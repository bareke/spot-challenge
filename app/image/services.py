import base64
import logging
from http import HTTPStatus
from uuid import UUID, uuid4

from azure.storage.blob import BlobServiceClient
from sqlalchemy import select

from app.settings.database import async_session
from app.settings.environment import settings

from .models import ImageModel
from .schemas import (
    CreateStorageSchema,
    GetImageSchema,
    ResponseGetBlobs,
    ResponseGetImage,
    ResponsePostImage,
)
from .tasks import upload_image


class ImageService:
    async def get(self, id: int) -> ResponseGetImage:
        """Retrieve an image from the database based on the provided ID.

        Args:
            id (int): The ID of the image to retrieve.

        Returns:
            ResponseGetImage: An instance of the ResponseGetImage
            class containing the retrieved image data, along with a
            status code and message.
        """

        async with async_session() as session:
            image = await session.get(ImageModel, id)

            if image:
                image_schema = GetImageSchema(
                    date=image.date,
                    id_camera=image.id_camera,
                    url=image.url,
                )

                return ResponseGetImage(
                    data=image_schema,
                    status_code=HTTPStatus.OK,
                    message="Get resource successful",
                )
            else:
                return ResponseGetImage(
                    status_code=HTTPStatus.NOT_FOUND,
                    message="Resource not found",
                    error="Not found",
                )


class StorageService:
    def __init__(self):
        self.container_name = settings.get("storage").get("container_name")
        self.blob_service_client = BlobServiceClient.from_connection_string(
            settings.get("storage").get("connection_string")
        )

    def generate_url(self, filename: str, extension: str) -> str:
        """Generate a URL for accessing a specific file in Azure Blob Storage.

        Args:
            filename (str): The name of the file.

        Returns:
            str: The generated URL for accessing the file.
        """

        url = f"https://spotproject.blob.core.windows.net/{self.container_name}/{filename}.{extension}"

        return url

    def list_all_blobs(self) -> ResponseGetBlobs:
        """List all blobs in a specified container of the Azure Blob Storage.

        Returns:
            ResponseGetBlobs: An instance of the ResponseGetImages class
            containing the list of blob names,
            status code (HTTPStatus.OK), and a success message.
        """

        container = self.blob_service_client.get_container_client(self.container_name)
        blob_list = container.list_blobs()

        return ResponseGetBlobs(
            data=[blob.name for blob in blob_list],
            status_code=HTTPStatus.OK,
            message="Get resources successfull",
        )

    async def process_image(self, storage: CreateStorageSchema) -> ResponsePostImage:
        """Process an image by uploading it to storage asynchronously,
        saving metadata to the database.

        Args:
            storage (CreateStorageSchema): An object containing
            the necessary information to process the image.

        Returns:
            ResponsePostImage: An instance of the ResponsePostImage
            class indicating the status of the image processing.
        """

        filename = uuid4()
        url_image = self.generate_url(filename, "jpg")

        upload_image.delay(filename, "jpg", storage.image_base64)

        image = ImageModel(
            id_camera=storage.id_camera,
            url=url_image,
            date=storage.date,
        )

        async with async_session() as session:
            session.add(image)
            await session.commit()
            await session.refresh(image)

        return ResponsePostImage(
            status_code=HTTPStatus.OK,
            message="Uploading image into storage",
        )

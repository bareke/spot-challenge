import base64
import logging
from http import HTTPStatus
from uuid import UUID, uuid4

from azure.storage.blob import BlobServiceClient

from app.settings.environment import settings

from .schemas import CreateStorageSchema, ResponseGetImages, ResponsePostImage
from .tasks import upload_image


class ImageService:
    def __init__(self):
        pass

    def get(self):
        pass

    def save(self):
        pass


class StorageService:
    def __init__(self):
        self.container_name = settings.get("storage").get("container_name")
        self.blob_service_client = BlobServiceClient.from_connection_string(
            settings.get("storage").get("connection_string")
        )

    def generate_url(self, filename: str) -> str:
        """Generate a URL for accessing a specific file in Azure Blob Storage.

        Args:
            filename (str): The name of the file.

        Returns:
            str: The generated URL for accessing the file.
        """

        url = f"https://spotproject.blob.core.windows.net/{self.container_name}/{filename}"

        return url

    def list_all_blobs(self) -> ResponseGetImages:
        """List all blobs in a specified container of the Azure Blob Storage.

        Returns:
            ResponseGetImages: An instance of the ResponseGetImages class
            containing the list of blob names,
            status code (HTTPStatus.OK), and a success message.
        """

        container = self.blob_service_client.get_container_client(self.container_name)
        blob_list = container.list_blobs()

        return ResponseGetImages(
            data=[blob.name for blob in blob_list],
            status_code=HTTPStatus.OK,
            message="Get resources successfull",
        )

    def process_image(self, storage: CreateStorageSchema) -> ResponsePostImage:
        """Process an image by uploading it to storage asynchronously.

        Args:
            storage (CreateStorageSchema): An object containing the necessary information to upload the image.

        Returns:
            ResponsePostImage: An instance of the ResponsePostImage class indicating the status of the image upload.
        """

        filename = uuid4()

        upload_image.delay(filename, "jpg", storage.image_base64)

        return ResponsePostImage(
            status_code=HTTPStatus.OK,
            message="Uploading image into storage",
        )

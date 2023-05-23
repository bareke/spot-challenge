import logging
from base64 import b64decode
from io import BytesIO
from uuid import UUID

from azure.storage.blob import BlobServiceClient

from app.settings.environment import settings
from app.settings.worker import celery


@celery.task
def upload_image(filename: UUID, extension: str, image_encode: str) -> None:
    """Uploads an image to Azure Blob Storage
    using the provided filename and Base64-encoded image data.

    Args:
        filename (UUID): The unique identifier of the image file.
        extension (str): The extension of the image file.
        image_encode (str): A string containing the Base64-encoded image data.

    Returns:
        Nones
    """
    image_binary = b64decode(image_encode)
    image = BytesIO(image_binary).getvalue()

    container_name = settings.get("storage").get("container_name")
    blob_service_client = BlobServiceClient.from_connection_string(
        settings.get("storage").get("connection_string")
    )

    try:
        blob_client = blob_service_client.get_blob_client(
            container=container_name, blob=f"{filename}.{extension}"
        )
        blob_client.upload_blob(image)

    except Exception as e:
        logging.error(e)

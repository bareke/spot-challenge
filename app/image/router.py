from fastapi import APIRouter

from .schemas import CreateStorageSchema, ResponseGetImages, ResponsePostImage
from .services import StorageService

router = APIRouter(
    prefix="/images",
    tags=["Images"],
)

storage_service = StorageService()


@router.get("", response_model=ResponseGetImages)
async def get_all_blobs():
    return storage_service.list_all_blobs()


@router.post("", response_model=ResponsePostImage)
async def upload_image(storage: CreateStorageSchema):
    return storage_service.process_image(storage)

from fastapi import APIRouter

from .models import ImageModel
from .schemas import (
    CreateStorageSchema,
    ResponseGetBlobs,
    ResponseGetImage,
    ResponsePostImage,
)
from .services import ImageService, StorageService

router = APIRouter(
    prefix="/images",
    tags=["Images"],
)

image_service = ImageService()
storage_service = StorageService()


@router.get("", response_model=ResponseGetBlobs)
async def get_all_blobs():
    return storage_service.list_all_blobs()


@router.get("/{id}", response_model=ResponseGetImage)
async def get_image(id: int):
    return await image_service.get(id)


@router.post("", response_model=ResponsePostImage)
async def upload_image(storage: CreateStorageSchema):
    return await storage_service.process_image(storage)

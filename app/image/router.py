from fastapi import APIRouter

router = APIRouter(
    prefix="/images",
    tags=["Images"],
)


@router.get("")
async def get_all_images():
    return True


@router.post("")
async def create_image():
    return True

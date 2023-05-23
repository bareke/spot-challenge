from datetime import datetime
from uuid import UUID

from humps import camelize
from pydantic import BaseModel as BaseSchema


def to_camelcase(value):
    return camelize(value)


class StorageBase(BaseSchema):
    date: datetime
    id_camera: int
    image_base64: str


class StorageSchema(StorageBase):
    class Config:
        # orm_mode = True
        alias_generator = to_camelcase
        allow_population_by_field_name = True


class GetImageSchema(StorageSchema):
    pass


class CreateStorageSchema(StorageSchema):
    pass


class ResponseSchema(BaseSchema):
    status_code: int
    message: str
    error: str = None

    class Config:
        alias_generator = to_camelcase
        allow_population_by_field_name = True


class ResponseGetImages(ResponseSchema):
    data: list[str] = None


class ResponsePostImage(ResponseSchema):
    pass

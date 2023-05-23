from sqlalchemy import Column, DateTime, Integer, String

from app.settings.database import Base


class ImageModel(Base):
    __tablename__ = "images"

    id = Column(Integer, primary_key=True, index=True)
    id_camera = Column(Integer)
    url = Column(String, nullable=False)
    date = Column(DateTime, nullable=False)

from sqlalchemy import Column, Integer, String, Float, Boolean
from database import Base


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True, server_default="1")
    name = Column(String, nullable=False)
    image_or_video = Column(String, nullable=False)
    description = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    is_available = Column(Boolean, default=True)

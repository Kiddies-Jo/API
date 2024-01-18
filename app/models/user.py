# app/models/user.py
from sqlalchemy import Boolean, Column, Integer, String, DateTime
from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True, server_default="1")
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    date_of_birth = Column(DateTime, nullable=False)
    cities = Column(String, nullable=False)
    address_location = Column(String, nullable=False)
    is_suspended = Column(Boolean, default=False)

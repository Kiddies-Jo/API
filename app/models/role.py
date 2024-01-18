from sqlalchemy import Column, Enum
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class RoleEnum(str, Enum):
    admin = "Admin"
    user = "User"


class Role(Base):
    __tablename__ = 'roles'

    role = Column(Enum(RoleEnum), nullable=False)

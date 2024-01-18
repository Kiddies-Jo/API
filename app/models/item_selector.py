from sqlalchemy import Column, Integer, ForeignKey, String
from database import Base


class ItemUserSelector(Base):
    __tablename__ = "item_user_selectors"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True, server_default="1")
    color = Column(String, nullable=False)
    number_of_items = Column(Integer, default=1)
    user_id = Column(Integer, ForeignKey("users.id"))
    item_id = Column(Integer, ForeignKey("items.id"))

from sqlalchemy.orm import Session

from app.models.item import Item
from app.models.models import ItemCreate
from sqlalchemy.orm.exc import NoResultFound


class ItemNotFoundException(Exception):
    pass


class ItemRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_item(self, item: ItemCreate):
        item_db = Item(name=item.name,
                       image_or_video=item.image_or_video,
                       description=item.description,
                       price=item.price
                       )
        self.db.add(item_db)
        self.db.commit()
        self.db.refresh(item_db)
        return item_db

    def get_all_items(self, page_number, items_per_page=9):
        # Calculate the offset based on the page number and items per page
        offset = (page_number - 1) * items_per_page

        # Query items with the specified limit and offset
        items = self.db.query(Item).limit(items_per_page).offset(offset).all()

        return items

    def suspended_by_id(self, item_id):
        try:
            self.db.query(Item).filter_by(id=item_id).update({Item.is_available: False}, synchronize_session=False)
            self.db.commit()
            return True
        except NoResultFound:
            return False

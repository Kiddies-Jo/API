from sqlalchemy.orm import Session
from app.models.item_selector import ItemUserSelector
from app.models.models import ItemUserSelectorCreate
from sqlalchemy.orm.exc import NoResultFound


class ItemSelectorRepository:
    def __init__(self, db: Session):
        self.db = db

    def add_item_selection(self, item_selector: ItemUserSelectorCreate):
        item_selector_db = ItemUserSelector(
            color=item_selector.color,
            number_of_items=item_selector.number_of_items,
            item_od=item_selector.item_id,
            user_id=item_selector.user_id
        )
        self.db.add(item_selector_db)
        self.db.commit()
        self.db.refresh(item_selector_db)
        return item_selector_db

    def delete_item_selection(self, item_selection_id: int, user_id: int):
        try:
            item_selection = self.db.query(ItemUserSelector).filter_by(
                item_id=item_selection_id, user_id=user_id
            ).one()
            self.db.delete(item_selection)
            self.db.commit()
            return True
        except NoResultFound:
            return False

    def get_selection_items(self, user_id):
        items = self.db.query(ItemUserSelector).filter_by(user_id=user_id).all()
        return items

    def update_item_selection(self, item_user_selector: ItemUserSelectorCreate):
        item_selector: ItemUserSelector = self.db.query(ItemUserSelector).filter(
            ItemUserSelector.item_id == item_user_selector.item_id,
            ItemUserSelector.user_id == item_user_selector.user_id
        ).one()
        item_selector.color = item_user_selector.color
        item_selector.number_of_items = item_user_selector.number_of_items
        self.db.commit()
        return item_selector

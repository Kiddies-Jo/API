from app.models.models import ItemUserSelectorCreate
from app.repositories.item_selector_repository import ItemSelectorRepository


class ItemUSerSelectorService:
    def __init__(self, item_selector_repository: ItemSelectorRepository):
        self.repo = item_selector_repository

    async def create_selection_item(self, item_selector: ItemUserSelectorCreate):
        return await self.repo.add_item_selection(item_selector)

    async def update_selection_item(self, item_selector: ItemUserSelectorCreate):
        return await self.repo.update_item_selection(item_user_selector=item_selector)

    async def get_selection_items(self, user_id: int):
        return await self.repo.get_selection_items(user_id)

    async def delete_selection_item(self, item_selection_id: int,user_id: int):
        return await self.repo.delete_item_selection(item_selection_id=item_selection_id,
                                                     user_id=user_id)

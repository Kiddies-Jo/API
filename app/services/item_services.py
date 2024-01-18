from app.models.models import ItemCreate
from app.repositories.item_repository import ItemRepository


class ItemServices:
    def __init__(self, item_repository: ItemRepository):
        self.repo = item_repository

    async def create_item(self, item: ItemCreate):
        return await self.repo.create_item(item)

    async def get_items(self, page_number):
        return await self.repo.get_all_items(page_number=page_number)

    async def suspended_item(self, item_id):
        return await self.repo.suspended_by_id(item_id=item_id)

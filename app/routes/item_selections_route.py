# Views
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from app.models.models import ItemUserSelectorCreate
from database import get_db
from app.services.item_selector_services import ItemUSerSelectorService
from app.repositories.item_selector_repository import ItemSelectorRepository
router = APIRouter()


@router.post('/', response_model=dict)
async def create_selection_item(selection_item: ItemUserSelectorCreate,  db: Session = Depends(get_db)):
    service = ItemUSerSelectorService(ItemSelectorRepository(db))
    selection_items = await service.create_selection_item(item_selector=selection_item)
    return {'result': selection_items}


@router.get('/', response_model=dict)
async def get_all_selection_item(user_id: int,  db: Session = Depends(get_db)):
    service = ItemUSerSelectorService(ItemSelectorRepository(db))
    selection_data = await service.get_selection_items(user_id)
    return {'result': selection_data} if selection_data else {"message": "PLease add items"}


@router.delete('/', response_model=dict)
async def delete_selection_item(user_id: int, item_id: int,  db: Session = Depends(get_db)):
    service = ItemUSerSelectorService(ItemSelectorRepository(db))
    is_deleted = await service.delete_selection_item(user_id=user_id, item_selection_id=item_id)
    if is_deleted:
        return {"message": "Deleted Successfully"}
    return HTTPException(status_code=400)


@router.put('/', response_model=dict)
async def update_selection_item(item_selector: ItemUserSelectorCreate,  db: Session = Depends(get_db)):
    service = ItemUSerSelectorService(ItemSelectorRepository(db))
    updated_value = await service.update_selection_item(item_selector=item_selector)
    return {'result': updated_value}

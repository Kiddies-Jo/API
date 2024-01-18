# Views
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.models.models import ItemCreate
from database import get_db
from app.services.item_services import ItemServices
from app.repositories.item_repository import ItemRepository
router = APIRouter()


@router.post('/', response_model=dict)
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    """
    This view for admin role to create a new item which need to display in the application
    :param item: ItemCreate
    :param db: kiddies Database
    :return: JSON
    """
    item_service = ItemServices(ItemRepository(db))
    item_service.create_item(item)
    return {"message": 'Item Created Successfully'}


@router.get("/{page_number}")
def get_items(page_number: int = 1, db: Session = Depends(get_db)):
    """
    this view for customer role used to return all items
    9 items per page
    :param page_number: Integer
    :param db: Database
    :return: List[Items]
    """
    item_service = ItemServices(ItemRepository(db))
    items = item_service.get_items(page_number)
    return {'items': items}


@router.put("/{item_id}")
def suspended_item(item_id: int, db: Session = Depends(get_db)):
    """
    :param item_id:
    :param db:
    :return:
    """
    item_service = ItemServices(ItemRepository(db))
    is_suspended = item_service.suspended_item(item_id)
    if is_suspended:
        return {"message": "Suspended Successfully"}
    else:
        raise HTTPException(status_code=401, detail="Invalid Credentials")

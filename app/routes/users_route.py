# Views
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from app.models.models import UserCreate, EmailAndPassword
from app.repositories.user_repository import UserRepository
from app.services.user_services import UserServices
from database import get_db
from app.security_jwt.security import JWTSecurity
router = APIRouter()


@router.post('/register', response_model=dict)
async def register(user: UserCreate, db: Session = Depends(get_db)):
    """
    :param user:  UserCreate
    :param db: Kiddies Database MYSQL
    :return: JSON
    """
    user_services = UserServices(UserRepository(db))

    # Check if the user already exists
    existing_user = await user_services.repo.get_user_by_email(user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")

    # Create a new user
    new_user: UserCreate = await user_services.create_user(user)
    if not new_user:
        raise HTTPException(status_code=500, detail="Failed to create user")

    jwt_security_service = JWTSecurity()
    jwt_token = jwt_security_service.create_jwt_token({"sub": {
        "email": new_user.email,
        "full_name": f"{new_user.first_name} {new_user.last_name}"
    }})

    return {"message": "User registered successfully", "token": jwt_token}


@router.post("/login", response_model=dict)
async def login(data: EmailAndPassword, db: Session = Depends(get_db)):
    """
    :param data: EmailAndPassword
    :param db: Kiddies Database
    :return: JSON
    """
    user_services = UserServices(UserRepository(db))
    is_valid_credential_user = await user_services.check_exist_user(data.email, data.password)
    if is_valid_credential_user:
        user: UserCreate = user_services.get_user_by_email(data.email)
        jwt_security_service = JWTSecurity()
        jwt_token = jwt_security_service.create_jwt_token({"sub": {
            "email": user.email,
            "full_name": f"{user.first_name} {user.last_name}"
        }})
        return {"message": "User registered successfully", "token": jwt_token}
    raise HTTPException(status_code=401, detail="Invalid Credentials")

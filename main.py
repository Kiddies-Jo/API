from fastapi import FastAPI, Depends

from app.dependencies.authentication import get_current_user
from app.routes import users_route, items_route, item_selections_route
from database import JWT_SECRET_KEY, ALGORITHM

app = FastAPI()

app.jwt_secret_key = JWT_SECRET_KEY
app.jwt_algorithm = ALGORITHM

app.dependency_overrides = {
    get_current_user: Depends(get_current_user)
}

app.include_router(users_route.router, prefix="/users", tags=["users"])
app.include_router(items_route.router, prefix="/items", tags=["items"])
app.include_router(item_selections_route.router, prefix="/item/selection", tags=["selections"])

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from app.security_jwt.security import JWTSecurity

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    jwt_security = JWTSecurity()
    user = jwt_security.verify_jwt_token(token)
    if user is None:
        raise credentials_exception
    return user

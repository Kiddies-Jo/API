from jose import JWTError, jwt
from typing import Union
from datetime import datetime, timedelta
from database import JWT_SECRET_KEY, ALGORITHM


class JWTSecurity:
    def __init__(self):
        TOKEN_EXPIRATION = timedelta(hours=2)

    def create_jwt_token(self, data: dict) -> str:
        expiration_datetime = datetime.utcnow() + self.TOKEN_EXPIRATION
        expiration_timestamp = expiration_datetime.timestamp()

        payload = {
            **data,
            "exp": expiration_timestamp
        }

        return jwt.encode(payload, JWT_SECRET_KEY, algorithm=ALGORITHM)

    @staticmethod
    def verify_jwt_token(token: str) -> Union[dict, None]:
        try:
            payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[ALGORITHM])
            return payload
        except JWTError:
            return None

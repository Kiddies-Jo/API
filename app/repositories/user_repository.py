from sqlalchemy.orm import Session
import bcrypt
from app.models.user import User


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_user_by_email(self, email: str):
        return self.db.query(User).filter(User.email == email).first()

    def create_user(self, user: User):
        if self.db.query(User).filter(User.email == user.email).first():
            return None
        db_user = User(email=user.email, first_name=user.first_name, last_name=user.last_name,
                       date_of_birth=user.date_of_birth, cities=user.cities, address_location=user.address_location,
                       hashed_password=bcrypt.hashpw(user.hashed_password.encode("utf-8"), bcrypt.gensalt()))
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def check_by_email_and_password(self, email: str, password: str):
        user: User = self.db.query(User).filter(User.email == email).first()
        hashed_password = bcrypt.checkpw(password, user.hashed_password)
        return user if hashed_password else None

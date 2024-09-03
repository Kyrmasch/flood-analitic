from sqlalchemy.orm import Session
from models.user import User


def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()


def get_user_by_id(db: Session, id: int):
    return db.query(User).filter(User.id == id).first()

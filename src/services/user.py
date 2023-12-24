from sqlalchemy.orm import Session

from models.user import User
from dto import user


def create_user(data: user.User, db: Session):
    user = User(username=data.username)

    try:
        db.add(user)
        db.commit()
        db.refresh(user)
    except Exception as e:
        print(e)

    return user

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id==user_id).first()

def update_user(data: user.User, db: Session, user_id: int):
    user = db.query(User).filter(User.id==user_id).first()
    user.username = data.username

    db.add(user)
    db.commit()
    db.refresh(user)

    return user

def delete_user(db: Session, user_id: int):
    user = db.query(User).filter(User.id==user_id).delete()
    db.commit()

    return user

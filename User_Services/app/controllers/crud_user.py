from sqlmodel import Session, select
from app.models.user_models import UserModel, User
from app.database.db_connector import DB_SESSION


def user_add(user_details: UserModel, session: DB_SESSION):

    db_statement = select(user).where(User.user_email == user_details.user_email).where(User.user_password == user_details.user_password)

    db_user_info = session.exec(db_statement).one_or_none()
    if db_user_info:
        print('User already exist')
        # TODO: add exception here
    else:
        user= select(User)
        session.add(user)
        session.commit()
        session.refresh(user)
            
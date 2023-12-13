from datetime import datetime, timedelta

from jose import jwt
from passlib.context import CryptContext
from pydantic import EmailStr
from sqlalchemy import select

from src.config import CONFIG
from src.database import async_session_maker
from src.exceptions import IncorrectEmailOrPassword
from src.models import UserAccount

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(hours=3)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, CONFIG.SECRET_KEY_jwt, algorithm=CONFIG.ALGORITHM)
    return encoded_jwt


async def authenticate_user(email: EmailStr, password: str):
    async with async_session_maker() as session:
        query = select(UserAccount).filter_by(email=email)
        user = await session.execute(query).scalar_one_or_none()
    if user and verify_password(password, user.hashed_password):
        return user
    else:
        raise IncorrectEmailOrPassword

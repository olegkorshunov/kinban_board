from datetime import datetime

from fastapi import Depends, Request
from jose import JWTError, jwt
from sqlalchemy import select

from exceptions import (
    AuthTokenExpier,
    IncorrectTokenFormat,
    TokenAbsent,
    UserDataNotFound,
)
from src.auth.auth import async_session_maker
from src.config import CONFIG
from src.models.user_account import UserAccount

access_token = "kanban_board_token"


def get_access_token(request: Request):
    access_token_jwt = request.cookies.get(access_token)
    if not access_token_jwt:
        raise TokenAbsent
    return access_token_jwt


async def get_current_user(access_token_jwt: str = Depends(get_access_token)):
    try:
        payload = jwt.decode(access_token_jwt, CONFIG.SECRET_KEY_jwt, algorithms=CONFIG.ALGORITHM)
    except JWTError:
        raise IncorrectTokenFormat
    expire = payload.get("exp")
    if not expire or int(expire) < datetime.utcnow().timestamp():
        raise AuthTokenExpier
    user_id = payload.get("sub")
    if not user_id:
        raise UserDataNotFound

    async with async_session_maker() as session:
        query = select(UserAccount).filter_by(id=user_id)
        user = await session.execute(query).scalar_one_or_none()

    if not user:
        raise UserDataNotFound
    return user

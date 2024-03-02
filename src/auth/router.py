from fastapi import APIRouter, Response
from sqlalchemy import select
from src.models.user_account import UserAccount

from src.schemas.auth import SUserLogin, SUserRegistration
from src.database import async_session_maker

router = APIRouter(tags=["auth"], prefix="/auth")


@router.post("/registration")
async def user_registration(user: SUserRegistration):
    async with async_session_maker() as session:
        stmt = select(UserAccount).filter_by(email=user.email)


#     existig_user = await DaoAuth.find_one_or_none(email=user_data.email)
#     if existig_user:
#         raise HttpException.UserAlredyExis
#     hashed_password = get_password_hash(password=user_data.password)
#     await DaoAuth.insert(email=user_data.email, hashed_password=hashed_password)


# @router.post("/login")
# async def login_user(response: Response, user_data: SUserLogin):
#     user = await authenticate_user(user_data.email, user_data.password)
#     access_token_jwt = create_access_token({"sub": str(user.id)})
#     response.set_cookie(access_token, access_token_jwt)
#     return access_token


# @router.post("/logout")
# async def logout_user(response: Response):
#     response.delete_cookie(access_token)

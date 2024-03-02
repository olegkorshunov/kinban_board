from pydantic import BaseModel, EmailStr


class SBaseUser(BaseModel):
    email: EmailStr

    class Config:
        orm_mode = True


class SUserRegistration(SBaseUser):
    password: str


class SUserLogin(SBaseUser):
    password: str

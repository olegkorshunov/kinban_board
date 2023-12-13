from fastapi import HTTPException, status


class BaseException(HTTPException):
    status_code = 500
    detail = ""

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class UserAlredyExis(BaseException):
    status_code = status.HTTP_409_CONFLICT
    detail = "User alredy exist"


class IncorrectEmailOrPassword(BaseException):
    status_code = status.HTTP_409_CONFLICT
    detail = "Incorrect email or password"


class AuthTokenExpier(BaseException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Auth token has expired"


class TokenAbsent(BaseException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Token is absent"


class IncorrectTokenFormat(BaseException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Incorrect token format"


class UserDataNotFound(BaseException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "User data not found"

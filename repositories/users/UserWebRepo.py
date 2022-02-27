import requests

from repositories.users.Errors import UserIsExists
from repositories.users.UserEntity import UserEntity, UserRegistrationEntity, UserLoginEntity

USER_SERVER_URI = "http://localhost:8888"


class UserWebRepo:
    """Repository for UserServer"""

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({"token": ""})

    @property
    def token(self):
        return self.session.headers["token"]

    @token.setter
    def token(self, value: str):
        self.session.headers.update({"token": value})

    def add(self, user: UserRegistrationEntity) -> str:
        resp = self.session.post(USER_SERVER_URI, json=user.dict())
        if resp.status_code == 201:
            return resp.headers.get("token")
        elif resp.status_code == 400:
            raise ValueError()
        elif resp.status_code == 208:
            raise UserIsExists()

    def check(self) -> bool:
        resp = self.session.options(USER_SERVER_URI)
        return resp.status_code == 202

    def info(self) -> UserEntity:
        resp = self.session.get(USER_SERVER_URI)
        return UserEntity(**resp.json())

    def auth(self, user: UserLoginEntity) -> str:
        resp = self.session.patch(USER_SERVER_URI, json=user.dict())
        if resp.status_code == 200:
            return resp.headers.get("token")
        else:
            raise ValueError()

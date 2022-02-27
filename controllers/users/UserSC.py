from typing import Optional, Awaitable

import pydantic
import pymysql
import tornado.web

from repositories.users.UserDbRepo import UserDbRepo
from repositories.users.UserEntity import UserRegistrationEntity, UserLoginEntity


class UserSC(tornado.web.RequestHandler):
    """Server Controller for UserServer"""

    @property
    def db(self) -> UserDbRepo:
        return self.application.db

    def data_received(self, chunk: bytes) -> Optional[Awaitable[None]]:
        return super().data_received(chunk)

    def post(self):
        try:
            self.set_header('Token', self.db.add(UserRegistrationEntity.parse_raw(self.request.body.decode())))
            self.set_status(201)
        except pydantic.ValidationError:
            self.set_status(400)
        except pymysql.IntegrityError:
            self.set_status(208)

    def options(self):
        token = self.request.headers.get('Token')
        if token is not None:
            self.set_status(202 if self.db.check(token) else 423)
        else:
            self.set_status(403)

    def patch(self):
        try:
            self.set_header('Token', self.db.auth(UserLoginEntity.parse_raw(self.request.body.decode())))
            self.set_status(200)
        except pydantic.ValidationError:
            self.set_status(400)

    def get(self):
        self.options()
        if self.get_status() != 202:
            return

        self.write(self.db.info(self.request.headers.get('Token')).dict())

"""
methods:
- check
- add
- info
- auth
"""
import tornado.web

from controllers.users.UserSC import UserSC
from repositories.users.UserDbRepo import USER_DATABASE_SETTINGS, UserDbRepo


class UserServer(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", UserSC),
        ]
        settings = dict(
            # template_path=os.path.join(os.path.dirname(__file__), "templates"),
            # static_path=os.path.join(os.path.dirname(__file__), "static"),
            xsrf_cookies=False,
            cookie_secret="11oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
        )
        tornado.web.Application.__init__(self, handlers, **settings)

        self.db = UserDbRepo()

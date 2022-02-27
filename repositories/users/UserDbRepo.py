import pymysql

from repositories.users.UserEntity import UserRegistrationEntity, UserEntity, UserLoginEntity
from repositories.users.UserRepo import UserRepo
import random
import string

USER_DATABASE_SETTINGS = dict(
    host="localhost",
    port=3306,
    user="root",
    password="andrey2003",
    database="userrepo",
    autocommit=False
)


class UserDbRepo(UserRepo):
    def __init__(self):
        self.connection = pymysql.connect(**USER_DATABASE_SETTINGS)

    def add(self, user: UserRegistrationEntity) -> str:
        with self.connection.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute("INSERT INTO userrepo.Users(first_name, last_name, patronymic) "
                           f"VALUE ('{user.first_name}', '{user.last_name}', '{user.patronymic}')")

            cursor.execute("INSERT INTO userrepo.authdata(user, email, password) "
                           f"VALUE (last_insert_id(), '{user.email}', '{user.password}')")
        self.connection.commit()
        return self.auth(user)

    def check(self, token: str) -> bool:
        with self.connection.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute(f"select count(*) != 0 as unlocked from userrepo.tokens where token='{token}'")
            return bool(cursor.fetchone()["unlocked"])

    def info(self, token:str) -> UserEntity:
        with self.connection.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute("select id, full_name as name, email "
                           "from userrepo.users "
                           "inner join userrepo.tokens on users.id = tokens.user "
                           "inner join userrepo.authdata a on users.id = a.user "
                           f"where tokens.token = '{token}'")

            return UserEntity(**cursor.fetchone())

    def auth(self, user: UserLoginEntity) -> str:
        with self.connection.cursor(pymysql.cursors.DictCursor) as cursor:
            token = ''.join([random.choice(string.ascii_letters) for n in range(25)])
            cursor.execute(
                "insert into userrepo.tokens(token, user) "
                f"select '{token}', user "
                f"from userrepo.authdata where email='{user.email}' and password='{user.password}'")
            self.connection.commit()
        return token

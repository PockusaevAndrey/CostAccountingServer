from controllers.users.UserEntity import UserEntity, UserRegistrationEntity, UserLoginEntity


class UserRepo:
    """Repository for UserServer"""

    def add(self, user: UserRegistrationEntity) -> str:
        pass

    def check(self, token: str) -> bool:
        pass

    def info(self) -> UserEntity:
        pass

    def auth(self, token: UserLoginEntity) -> str:
        pass

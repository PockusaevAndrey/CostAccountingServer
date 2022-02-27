from abc import abstractmethod, ABCMeta

from repositories.users.UserEntity import UserEntity, UserRegistrationEntity, UserLoginEntity


class UserRepo(metaclass=ABCMeta):
    """Repository for UserServer"""

    @abstractmethod
    def add(self, user: UserRegistrationEntity) -> str:
        pass

    @abstractmethod
    def check(self, token: str) -> bool:
        pass

    @abstractmethod
    def info(self, token: str) -> UserEntity:
        pass

    @abstractmethod
    def auth(self, token: UserLoginEntity) -> str:
        pass

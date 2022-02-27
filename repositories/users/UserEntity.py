from pydantic import BaseModel, EmailStr, validator


class UserEntity(BaseModel):
    id: int
    name: str
    email: EmailStr


class UserLoginEntity(BaseModel):
    email: EmailStr
    password: str


class UserRegistrationEntity(UserLoginEntity):
    first_name: str
    last_name: str
    patronymic: str

    @validator('first_name', 'last_name', 'patronymic')
    def title_names(cls, value):
        return value.title()

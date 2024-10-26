from typing import Annotated
from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer


fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "fakehashedsecret",
        "disabled": False,
    },
    "alice": {
        "username": "alice",
        "full_name": "Alice Wonderson",
        "email": "alice@example.com",
        "hashed_password": "fakehashedsecret2",
        "disabled": True,
    },
}

async def dobro(num: int):
    return num*2

async def wrapper_dobro():
    return await dobro(2)

async def example(login: Annotated[int, Depends(wrapper_dobro)]):
    print(login)

example()

# user = fake_users_db.get("alice")
# print(user)
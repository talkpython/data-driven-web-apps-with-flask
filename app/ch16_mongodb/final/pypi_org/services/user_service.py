from typing import Optional

import bson
from passlib.handlers.sha2_crypt import sha512_crypt as crypto
from pypi_org.nosql.users import User


def get_user_count() -> int:
    return User.objects().count()


def find_user_by_email(email: str) -> Optional[User]:
    return User.objects().filter(email=email).first()


def create_user(name: str, email: str, password: str) -> Optional[User]:
    if find_user_by_email(email):
        return None

    user = User()
    user.email = email
    user.name = name
    user.hashed_password = hash_text(password)

    user.save()

    return user


def hash_text(text: str) -> str:
    hashed_text = crypto.encrypt(text, rounds=171204)
    return hashed_text


def verify_hash(hashed_text: str, plain_text: str) -> bool:
    return crypto.verify(plain_text, hashed_text)


def login_user(email: str, password: str) -> Optional[User]:
    user = find_user_by_email(email)
    if not user:
        return None

    if not verify_hash(user.hashed_password, password):
        return None

    return user


def find_user_by_id(user_id: bson.ObjectId) -> Optional[User]:
    user = User.objects().filter(id=user_id).first()
    return user

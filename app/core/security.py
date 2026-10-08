from datetime import datetime, timedelta, timezone
from pathlib import Path

import jwt
from passlib.context import CryptContext

from app.core.config import (
    ACCESS_TOKEN_EXPIRE_MINUTES,
    JWT_ALGORITHM,
    PRIVATE_KEY_PATH,
    PUBLIC_KEY_PATH,
    REFRESH_TOKEN_EXPIRE_DAYS,
)

password_hashing_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    return password_hashing_context.hash(password)


def verify_password(password: str, hashed_password) -> bool:
    return password_hashing_context.verify(password, hashed_password)


def load_private_key() -> str:
    return Path(PRIVATE_KEY_PATH).read_text()


def load_public_key() -> str:
    return Path(PUBLIC_KEY_PATH).read_text()


def create_access_token(user_id: int, role: str) -> str:
    now = datetime.now(timezone.utc)
    expire = now + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    payload = {
        "sub": str(user_id),
        "role": role,
        "type": "access",
        "iat": now,
        "exp": expire,
    }
    private_key = load_private_key()
    token = jwt.encode(payload, private_key, algorithm=JWT_ALGORITHM)
    return token


def create_refresh_token(user_id: int, role: str) -> str:
    now = datetime.now(timezone.utc)
    expire = now + timedelta(minutes=REFRESH_TOKEN_EXPIRE_DAYS)
    payload = {
        "sub": str(user_id),
        "role": role,
        "type": "access",
        "iat": now,
        "exp": expire,
    }
    private_key = load_private_key()
    token = jwt.encode(payload, private_key, algorithm=JWT_ALGORITHM)
    return token


def verify_token(token: str) -> dict:
    public_key = load_public_key()
    payload = jwt.decode(token, public_key, algorithms=JWT_ALGORITHM)
    return payload

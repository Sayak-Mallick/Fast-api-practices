from passlib.context import CryptContext

password_hashing_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    return password_hashing_context.hash(password)


def verify_password(password: str, hashed_password) -> bool:
    return password_hashing_context.verify(password, hashed_password)

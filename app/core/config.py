from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

PRIVATE_KEY_PATH = BASE_DIR / "keys" / "private.pem"
PUBLIC_KEY_PATH = BASE_DIR / "keys" / "public.pem"

ACCESS_TOKEN_EXPIRE_MINUTES = 15
REFRESH_TOKEN_EXPIRE_DAYS = 7

JWT_ALGORITHM = "RS256"
import magic
from passlib.context import CryptContext

from fastapi import HTTPException


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(password: str, hashed_password: str) -> bool:
    return pwd_context.verify(password, hashed_password)

def validate_non_empty_fields(data: dict) -> None:
    for key, value in data.items():
        if not value or not value.strip():
            raise HTTPException(
                status_code=422,
                detail=f"Field '{key}' cannot be empty"
            )
 
def check_file_format(file_content) -> bool:
    mime = magic.Magic()
    file_type = mime.from_buffer(file_content)

    if "image" in file_type:
        return True
    return False


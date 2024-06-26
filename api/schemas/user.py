from pydantic import BaseModel
from uuid import UUID

class User(BaseModel):
    name: str
    email: str
    hashed_password: str


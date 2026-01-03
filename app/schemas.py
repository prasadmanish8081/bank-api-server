from pydantic import BaseModel
from typing import List

class BranchBase(BaseModel):
    ifsc: str
    branch: str
    city: str
    state: str

    class Config:
        orm_mode = True


class BankBase(BaseModel):
    id: int
    name: str
    branches: List[BranchBase] = []

    class Config:
        orm_mode = True

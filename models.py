import strawberry
from dataclasses import dataclass
from typing import Optional


@strawberry.type
@dataclass
class Patient:
    id: int
    name: str
    age: int
    phone: str
    email: str
    address: str

@strawberry.input
class InsertPatient:
    id: int
    name: str
    age: int
    phone: str
    email: str
    address: str

@strawberry.type
class Response:
    message: str

@strawberry.input
class UpdatePatient:
    id:int
    name: Optional[str]=None
    age: Optional[int]=None
    phone: Optional[str]=None
    email: Optional[str]=None
    address: Optional[str]=None

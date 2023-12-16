"""
Nested models and lists
=========================
"""
from pydantic import BaseModel, ValidationError
from typing import List


class Address(BaseModel):
    street: str
    building: int


class Person(BaseModel):
    age: int
    name: str
    is_married: bool
    address: Address
    languages: List[str]


# Good data
# data = {
#     'age': 10,
#     'name': 'John',
#     'is_married': False,
#     'address': {
#         'street': 'st street',
#         'building': 10
#     },
#     'languages': ['pt-pt', 'en-us']
# }

# Corrupted data
data = {
    'age': 10,
    'name': 'John',
    'is_married': False,
    'address': {
        'street': 'st street',
        'building': 'test'
    },
    'languages': [{}, 'en-us']
}

try:
    person = Person(**data)
    print(person.model_dump())
except ValidationError as e:
    print("Exception as str:")
    print(e)
    print("Exception as json:")
    print(e.json(indent=2))

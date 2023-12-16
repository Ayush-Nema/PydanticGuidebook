"""
Introduction
==============
General introduction to Pydantic
"""

from pydantic import BaseModel, ValidationError


class Person(BaseModel):
    age: int
    name: str
    is_married: bool


# This example works perfectly fine (validation passes)
# data = {
#     'name': 'John',
#     'age': 20,
#     'is_married': False
# }

# Yields error as age isn't `int` and is_married isn't `bool`. (validation fails with 2 errors)
data = {
    'age': "test",
    'is_married': False
}

person = Person(**data)

try:
    person = Person(**data)
    print(person.model_dump())
    # use the data
except ValidationError as e:
    print(e)

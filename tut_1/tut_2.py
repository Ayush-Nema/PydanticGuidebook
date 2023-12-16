"""
Error handling
===============
The errors method returns a list of errors with the following properties:
loc: the error location
type: the type of the error
msg: a human-readable message explaining the error
"""
from pydantic import BaseModel, ValidationError


class Person(BaseModel):
    age: int
    name: str
    is_married: bool


data = {
    'age': "test",
    'is_married': False
}

try:
    person = Person(**data)
    print(person.model_dump())

except ValidationError as e:
    # Pretty printing of validation error(s) as JSON
    print(e.json(indent=2))

    # Description of individual errors
    errors = e.errors()
    print(errors)

    print()
    print(errors[0])

    print()
    print(errors[1]["loc"])
    print(errors[1]["msg"])
    print(errors[1]["type"])

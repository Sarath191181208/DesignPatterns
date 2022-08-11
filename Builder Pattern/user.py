from datetime import datetime


class User:
    def __init__(self) -> None:
        self.name: str
        self.date_of_birth: datetime

    def set_name(self, name: str):
        self.name = name
        return self

    def set_date_of_birth(self, dob: datetime):
        self.date_of_birth = dob
        return self

    def __str__(self) -> str:
        return f"Name: {self.name} Date of Birth: {self.date_of_birth}"

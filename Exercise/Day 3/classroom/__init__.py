# __init__.py
from .person import Person
from .student import Student
from .teacher import Teacher
class Person:
    def __init__(self, firstname, lastname):
        """
        Constructor that initializes first name and last name.
        """
        self.firstname = firstname
        self.lastname = lastname

    def get_full_name(self):
        """
        Returns the full name (firstname + lastname).
        """
        return f"{self.firstname} {self.lastname}"

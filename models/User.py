from typing import TYPE_CHECKING
from interfaces.IUser import IUser


if TYPE_CHECKING:
    from models.contact import Contact

class User(IUser):
    def __init__(self, id_user: int, first_name: str, last_name: str, email: str, phone: str, contact: 'Contact'):
        self._id_user           = id_user
        self._first_name        = first_name
        self._last_name         = last_name
        self._email             = email
        self._phone             = phone
        self._contact           = contact

    @property
    def id_user(self):
        return self._id_user

    @id_user.setter
    def id_user(self, value):
        self._id_user = value

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value

    @property
    def contact(self):
        return self._contact

    @contact.setter
    def contact(self, value):
        self._contact = value


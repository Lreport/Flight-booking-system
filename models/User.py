from typing import TYPE_CHECKING
from interfaces.Iuser import Iuser


if TYPE_CHECKING:
    from models.contact import Contact

class User(Iuser):
    def __init__(self, id_user: int, first_name: str, last_name: str, contact: 'Contact'):
        self._id_user           = id_user
        self._first_name        = first_name
        self._last_name         = last_name
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
    def contact(self):
        return self._contact

    @contact.setter
    def contact(self, value):
        self._contact = value


    
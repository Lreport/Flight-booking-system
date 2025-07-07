from typing import TYPE_CHECKING
from interfaces.Iuser import Iuser


if TYPE_CHECKING:
    from models.contact import Contact

class User(Iuser):
    def __init__(self, id_user: int, name: str, contact=None):
        self._id_user = id_user
        self._name = name
        self._contact = contact

    @property
    def id_user(self):
        return self._id_user

    @id_user.setter
    def id_user(self, value):
        self._id_user = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def contact(self):
        return self._contact

    @contact.setter
    def contact(self, value):
        self._contact = value


    

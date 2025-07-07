from interfaces.Icrew import Icrew
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.contact import Contact


class Crew(Icrew):
    def __init__(self, id_user:int, first_name:str, last_name:str, contact: 'Contact', role:str):
        self._id_user       = id_user
        self._first_name    = first_name
        self._last_name     = last_name
        self._contact       = contact
        self._role          = role

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

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, value):
        self._role = value

    def __str__(self):
        return f"{self._role}: {self.first_name} {self.last_name} (ID: {self.id_user})"


class Pilot(Crew):
    def __init__(self, id_user:int, first_name:str, last_name:str, contact: 'Contact', role:str = 'Pilot'):
        super().__init__(id_user, first_name, last_name, contact, role)


class Copilot(Crew):
    def __init__(self, id_user:int, first_name:str, last_name:str, contact: 'Contact', role:str = 'Copilot'):
        super().__init__(id_user, first_name, last_name, contact, role)


class Commissar(Crew):
    def __init__(self, id_user:int, first_name:str, last_name:str, contact: 'Contact', role:str = 'Commissar'):
        super().__init__(id_user, first_name, last_name, contact, role)
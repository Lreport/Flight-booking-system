from models.user import User
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.contact import Contact


class Crew(User):
    def __init__(self, id_user:int, first_name:str, last_name:str, contact: 'Contact', role:str):
        super().__init__(id_user, first_name, last_name, contact)
        self._role = role

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, value):
        self._role = value


class Pilot(Crew):
    def __init__(self, id_user:int, first_name:str, last_name:str, contact: 'Contact', role:str = 'Pilot'):
        super().__init__(id_user, first_name, last_name, contact, role)


class Copilot(Crew):
    def __init__(self, id_user:int, first_name:str, last_name:str, contact: 'Contact', role:str = 'Copilot'):
        super().__init__(id_user, first_name, last_name, contact, role)


class Commissar(Crew):
    def __init__(self, id_user:int, first_name:str, last_name:str, contact: 'Contact', role:str = 'Commissar'):
        super().__init__(id_user, first_name, last_name, contact, role)
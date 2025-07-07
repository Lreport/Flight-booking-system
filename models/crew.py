from typing import TYPE_CHECKING
from models.user import User

if TYPE_CHECKING:
    from models.contact import Contact


class Crew(User):
    def __init__(self, id_user: int, name: str, contact=None, role: str = "Crew"):
        super().__init__(id_user, name, contact)
        self._role = role

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, value):
        self._role = value

    def __str__(self):
        return f"{self._role}: {self.name} (ID: {self.id_user})"


class Pilot(Crew):
    def __init__(self, id_user: int, name: str, contact=None, role: str = 'Pilot'):
        super().__init__(id_user, name, contact, role)


class Copilot(Crew):
    def __init__(self, id_user: int, name: str, contact=None, role: str = 'Copilot'):
        super().__init__(id_user, name, contact, role)


class Commissar(Crew):
    def __init__(self, id_user: int, name: str, contact=None, role: str = 'Commissar'):
        super().__init__(id_user, name, contact, role)
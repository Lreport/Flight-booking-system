from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.User import User

class Crew:
    def __init__(self, id: User, first_name: str, last_name: str, role: str):
        self.__id = User
        self.__first_name = first_name
        self.__last_name = last_name
        self.__role = role

    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value

    @property
    def _first_name(self):
        return self.__first_name

    @_first_name.setter
    def _first_name(self, value):
        self.__first_name = value

    @property
    def _last_name(self):
        return self.__last_name

    @_last_name.setter
    def _last_name(self, value):
        self.__last_name = value

    @property
    def _role(self):
        return self.__role

    @_role.setter
    def _role(self, value):
        self.__role = value


    def __str__(self):
        return f"Crew ID: {self._id}, Name: {self._first_name} {self._last_name}, Role: {self._role}"

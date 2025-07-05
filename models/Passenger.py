from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.User import User
    from models.User import User

class Passenger:
    def __init__(self, id:User, firstName:str, lastName:str, age:int, gender:str, passport: User):
        self.__id = id
        self.__firstName = firstName
        self.__last_Name = lastName
        self.__age = age
        self.__gender = gender
        self.__passport = User

    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value

    @property
    def _firstName(self):
        return self.__firstName

    @_firstName.setter
    def _firstName(self, value):
        self.__firstName = value

    @property
    def _last_Name(self):
        return self.__last_Name

    @_last_Name.setter
    def _last_Name(self, value):
        self.__last_Name = value

    @property
    def _age(self):
        return self.__age

    @_age.setter
    def _age(self, value):
        self.__age = value

    @property
    def _gender(self):
        return self.__gender

    @_gender.setter
    def _gender(self, value):
        self.__gender = value

    @property
    def _passport(self):
        return self.__passport

    @_passport.setter
    def _passport(self, value):
        self.__passport = value

    def __str__(self):
        return f'Passenger ID: {self._id}, Name: {self._firstName} {self._last_Name}, Age: {self._age}' 
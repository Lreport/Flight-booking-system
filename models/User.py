from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.Contact import Contact

class User:
    def __init__(self,id:int, userName:str, password:str, firstName: str, lastNama: str, contact: Contact):
        self.__idUser= id
        self.__userName= userName
        self.__password= password
        self.__firstName= firstName
        self.__lastName= lastNama
        self.__contact= contact

    @property
    def _idUser(self):
        return self.__idUser

    @_idUser.setter
    def _idUser(self, value):
        self.__idUser = value

    @property
    def _userName(self):
        return self.__userName

    @_userName.setter
    def _userName(self, value):
        self.__userName = value

    @property
    def _password(self):
        return self.__password

    @_password.setter
    def _password(self, value):
        self.__password = value

    @property
    def _firstName(self):
        return self.__firstName

    @_firstName.setter
    def _firstName(self, value):
        self.__firstName = value

    @property
    def _lastName(self):
        return self.__lastName

    @_lastName.setter
    def _lastName(self, value):
        self.__lastName = value

    @property
    def _contact(self):
        return self.__contact

    @_contact.setter
    def _contact(self, value):
        self.__contact = value




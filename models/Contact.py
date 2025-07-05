from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.Address import Address


class Contact:
    def __init__(self, id:int, address: Address, email:str, phoneNumber:str):
        self.__idCotact = id
        self.__address = address
        self.__email = email
        self.__phoneNumber = phoneNumber

    @property
    def _idCotact(self):
        return self.__idCotact

    @_idCotact.setter
    def _idCotact(self, value):
        self.__idCotact = value

    @property
    def _address(self):
        return self.__address

    @_address.setter
    def _address(self, value):
        self.__address = value

    @property
    def _email(self):
        return self.__email

    @_email.setter
    def _email(self, value):
        self.__email = value

    @property
    def _phoneNumber(self):
        return self.__phoneNumber

    @_phoneNumber.setter
    def _phoneNumber(self, value):
        self.__phoneNumber = value


    def __str__(self):
        return f"Contact ID: {self._idCotact}, Address: {self._address._idContact}, Email: {self._email}, Phone Number: {self._phoneNumber}"
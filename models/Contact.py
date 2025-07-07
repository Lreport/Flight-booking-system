from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from models.address import Address

class Contact:
    def __init__(self, id_contact: int = None, address: 'Address' = None, id_address: int = None, email: str = None, phone_number: str = None):
        self._id_contact    = id_contact
        self._address       = address
        self._id_address    = id_address
        self._email         = email
        self._phone_number  = phone_number

    @property
    def id_contact(self):
        return self._id_contact

    @id_contact.setter
    def id_contact(self, value):
        self._id_contact = value

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value

    @property
    def id_address(self):
        return self._id_address
    
    @id_address.setter
    def id_address(self, value):
        self._id_address = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value):
        self._phone_number = value

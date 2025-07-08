from typing import TYPE_CHECKING, Optional
from interfaces.Icontact import Icontact


if TYPE_CHECKING:
    from models.address import Address

class Contact(Icontact):
    def __init__(self, id_contact=None, address=None, id_address=None, email=None, phone_number=None):
        self._id_contact = id_contact
        self._address = address
        self._id_address = id_address
        self._email = email
        self._phone_number = phone_number

    @property
    def id_contact(self) -> Optional[int]:
        return self._id_contact

    @id_contact.setter
    def id_contact(self, value: Optional[int]):
        self._id_contact = value

    @property
    def address(self) -> Optional['Address']:
        return self._address

    @address.setter
    def address(self, value: Optional['Address']):
        self._address = value

    @property
    def id_address(self) -> Optional[int]:
        return self._id_address
    
    @id_address.setter
    def id_address(self, value: Optional[int]):
        self._id_address = value

    @property
    def email(self) -> Optional[str]:
        return self._email

    @email.setter
    def email(self, value: Optional[str]):
        self._email = value

    @property
    def phone_number(self) -> Optional[str]:
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value: Optional[str]):
        self._phone_number = value

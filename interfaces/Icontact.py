from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.address import Address

class Icontact(ABC):
    #########################################################
    @property
    @abstractmethod
    def id_contact(self) -> int:
        """Get the contact ID."""
        pass

    @id_contact.setter
    @abstractmethod
    def id_contact(self, value: int):
        """Set the contact ID."""
        pass

    #########################################################
    @property
    @abstractmethod
    def address(self) -> 'Address':
        """Get the contact's address."""
        pass

    @address.setter
    @abstractmethod
    def address(self, value: 'Address'):
        """Set the contact's address."""
        pass

    #########################################################
    @property
    @abstractmethod
    def id_address(self) -> int:
        """Get the contact's address ID."""
        pass

    @id_address.setter
    @abstractmethod
    def id_address(self, value: int):
        """Set the contact's address ID."""
        pass
    
    #########################################################
    @property
    @abstractmethod
    def email(self) -> str:
        """Get the contact's email."""
        pass

    @email.setter
    @abstractmethod
    def email(self, value: str):
        """Set the contact's email."""
        pass

    #########################################################
    @property
    @abstractmethod
    def phone_number(self) -> str:
        """Get the contact's phone number."""
        pass

    @phone_number.setter
    @abstractmethod
    def phone_number(self, value: str):
        """Set the contact's phone number."""
        pass
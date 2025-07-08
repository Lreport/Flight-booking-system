from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from models.address import Address

class Icontact(ABC):
    #########################################################
    @property
    @abstractmethod
    def id_contact(self) -> Optional[int]:
        """Get the contact ID."""
        pass

    @id_contact.setter
    @abstractmethod
    def id_contact(self, value: Optional[int]):
        """Set the contact ID."""
        pass

    #########################################################
    @property
    @abstractmethod
    def address(self) -> Optional['Address']:
        """Get the contact's address."""
        pass

    @address.setter
    @abstractmethod
    def address(self, value: Optional['Address']):
        """Set the contact's address."""
        pass

    #########################################################
    @property
    @abstractmethod
    def id_address(self) -> Optional[int]:
        """Get the contact's address ID."""
        pass

    @id_address.setter
    @abstractmethod
    def id_address(self, value: Optional[int]):
        """Set the contact's address ID."""
        pass
    
    #########################################################
    @property
    @abstractmethod
    def email(self) -> Optional[str]:
        """Get the contact's email."""
        pass

    @email.setter
    @abstractmethod
    def email(self, value: Optional[str]):
        """Set the contact's email."""
        pass

    #########################################################
    @property
    @abstractmethod
    def phone_number(self) -> Optional[str]:
        """Get the contact's phone number."""
        pass

    @phone_number.setter
    @abstractmethod
    def phone_number(self, value: Optional[str]):
        """Set the contact's phone number."""
        pass
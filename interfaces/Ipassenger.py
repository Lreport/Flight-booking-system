from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.contact import Contact

class IPassenger(ABC):
    ########################################################
    @property
    @abstractmethod
    def id_user(self) -> int:
        """Get the user ID."""
        pass

    @id_user.setter
    @abstractmethod
    def id_user(self, value: int):
        """Set the user ID."""
        pass

    ########################################################
    @property
    @abstractmethod
    def first_name(self) -> str:
        """Get the user's first name."""
        pass

    @first_name.setter
    @abstractmethod
    def first_name(self, value: str):
        """Set the user's first name."""
        pass

    ########################################################
    @property
    @abstractmethod
    def last_name(self) -> str:
        """Get the user's last name."""
        pass

    @last_name.setter
    @abstractmethod
    def last_name(self, value: str):
        """Set the user's last name."""
        pass

    ########################################################
    @property
    @abstractmethod
    def contact(self) -> 'Contact':
        """Get the contact information of the passenger."""
        pass

    @contact.setter
    @abstractmethod
    def contact(self, value: 'Contact'):
        """Set the contact information of the passenger."""
        pass
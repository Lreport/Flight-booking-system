from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.contact import Contact

class IPassenger(ABC):
    ########################################################
    @property
    def id_user(self) -> int:
        """Get the passenger ID."""
        pass

    @id_user.setter
    @abstractmethod
    def id_user(self, value: int):
        """Set the passenger ID."""
        pass

    #######################################################
    @property
    def first_name(self) -> str:
        """Get the passenger's first name."""
        pass

    @first_name.setter
    @abstractmethod
    def first_name(self, value: str):
        """Set the passenger's first name."""
        pass

    #######################################################
    @property
    def last_name(self) -> str:
        """Get the passenger's last name."""
        pass

    @last_name.setter
    @abstractmethod
    def last_name(self, value: str):
        """Set the passenger's last name."""
        pass

    #######################################################
    @property
    def contact(self) -> 'Contact':
        """Get the passenger's contact information."""
        pass

    @contact.setter
    @abstractmethod
    def contact(self, value: 'Contact'):
        """Set the passenger's contact information."""
        pass
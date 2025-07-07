from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.contact import Contact


class Icrew(ABC):
    #########################################################
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
    #########################################################
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
    #########################################################
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
    #########################################################
    @property
    @abstractmethod
    def contact(self) -> 'Contact':
        """Get the user's contact information."""
        pass

    @contact.setter
    @abstractmethod
    def contact(self, value: 'Contact'):
        """Set the user's contact information."""
        pass
    #########################################################
    @property
    @abstractmethod
    def role(self) -> str:
        """Get the crew member's role."""
        pass

    @role.setter
    @abstractmethod
    def role(self, value: str):
        """Set the crew member's role."""
        pass
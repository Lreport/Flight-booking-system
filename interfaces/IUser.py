from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.contact import Contact


class Iuser(ABC):
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

    #######################################################
    @property
    @abstractmethod
    def name(self) -> str:
        """Get the user's name."""
        pass

    @name.setter
    @abstractmethod
    def name(self, value: str):
        """Set the user's name."""
        pass

    #######################################################
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


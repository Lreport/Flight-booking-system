from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.contact import Contact


class Iuser(ABC):
    ########################################################
    @property
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
    def first_name(self) -> str:
        """Get the user's first name."""
        pass

    @first_name.setter
    @abstractmethod
    def first_name(self, value: str):
        """Set the user's first name."""
        pass

    #######################################################
    @property
    def last_name(self) -> str:
        """Get the user's last name."""
        pass

    @last_name.setter
    @abstractmethod
    def last_name(self, value: str):
        """Set the user's last name."""
        pass

    #######################################################
    @property
    def email(self) -> str:
        """Get the user's email."""
        pass

    @email.setter
    @abstractmethod
    def email(self, value: str):
        """Set the user's email."""
        pass

    #######################################################
    @property
    def phone(self) -> str:
        """Get the user's phone number."""
        pass

    @phone.setter
    @abstractmethod
    def phone(self, value: str):
        """Set the user's phone number."""
        pass

    #######################################################
    @property
    def contact(self) -> 'Contact':
        """Get the user's contact information."""
        pass

    @contact.setter
    @abstractmethod
    def contact(self, value: 'Contact'):
        """Set the user's contact information."""
        pass


from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from models.contact import Contact
    from models.seat import Seat

class Ipassenger(ABC):
    ########################################################
    @property
    @abstractmethod
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
    @abstractmethod
    def name(self) -> str:
        """Get the passenger's name."""
        pass

    @name.setter
    @abstractmethod
    def name(self, value: str):
        """Set the passenger's name."""
        pass

    #######################################################
    @property
    @abstractmethod
    def contact(self) -> 'Contact':
        """Get the passenger's contact information."""
        pass

    @contact.setter
    @abstractmethod
    def contact(self, value: 'Contact'):
        """Set the passenger's contact information."""
        pass

    #######################################################
    @property
    @abstractmethod
    def assigned_seat(self) -> Optional['Seat']:
        """Get the seat assigned to the passenger."""
        pass

    @assigned_seat.setter
    @abstractmethod
    def assigned_seat(self, value: Optional['Seat']):
        """Set the seat assigned to the passenger."""
        pass
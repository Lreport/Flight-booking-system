from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from models.flight import Flight
    from models.passenger import Passenger


class Iseat(ABC):
    ########################################################
    @property
    @abstractmethod
    def id_seat(self) -> int:
        """Get the seat ID."""
        pass

    @id_seat.setter
    @abstractmethod
    def id_seat(self, value: int):
        """Set the seat ID."""
        pass

    ########################################################
    @property
    @abstractmethod
    def flight(self) -> 'Flight':
        """Get the flight associated with the seat."""
        pass

    @flight.setter
    @abstractmethod
    def flight(self, value: 'Flight'):
        """Set the flight associated with the seat."""
        pass

    ########################################################
    @property
    @abstractmethod
    def passenger(self) -> Optional['Passenger']:
        """Get the passenger assigned to the seat."""
        pass

    @passenger.setter
    @abstractmethod
    def passenger(self, value: Optional['Passenger']):
        """Set the passenger assigned to the seat."""
        pass
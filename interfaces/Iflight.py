from abc import ABC, abstractmethod
from models.passenger import Passenger
from models.crew import Crew

class IFlight(ABC):
    #########################################################
    @property
    @abstractmethod
    def id_flight(self) -> int:
        """Get the flight ID."""
        pass

    @id_flight.setter
    @abstractmethod
    def id_flight(self, value: int):
        """Set the flight ID."""
        pass
    #########################################################
    @property
    @abstractmethod
    def flight_number(self) -> str:
        """Get the flight number."""
        pass

    @flight_number.setter
    @abstractmethod
    def flight_number(self, value: str):
        """Set the flight number."""
        pass
    #########################################################
    @property
    @abstractmethod
    def origin(self) -> str:
        """Get the flight origin."""
        pass

    @origin.setter
    @abstractmethod
    def origin(self, value: str):
        """Set the flight origin."""
        pass
    #########################################################
    @property
    @abstractmethod
    def destination(self) -> str:
        """Get the flight destination."""
        pass

    @destination.setter
    @abstractmethod
    def destination(self, value: str):
        """Set the flight destination."""
        pass
    #########################################################
    @property
    @abstractmethod
    def departure_time(self) -> str:
        """Get the flight departure time."""
        pass

    @departure_time.setter
    @abstractmethod
    def departure_time(self, value: str):
        """Set the flight departure time."""
        pass
    #########################################################
    @property
    @abstractmethod
    def arrival_time(self) -> str:
        """Get the flight arrival time."""
        pass

    @arrival_time.setter
    @abstractmethod 
    def arrival_time(self, value: str):
        """Set the flight arrival time."""
        pass
    #########################################################
    @property
    @abstractmethod
    def price(self) -> float:
        """Get the flight price."""
        pass

    @price.setter
    @abstractmethod
    def price(self, value: float):
        """Set the flight price."""
        pass
    #########################################################
    @property
    @abstractmethod
    def passengers(self) -> list[Passenger]:
        """Get the list of passengers on the flight."""
        pass

    @passengers.setter
    @abstractmethod
    def passengers(self, value: list[Passenger]):
        """Set the list of passengers on the flight."""
        pass
    #########################################################
    @property
    @abstractmethod
    def crew(self) -> list[Crew]:
        """Get the list of crew members on the flight."""
        pass

    @crew.setter
    @abstractmethod
    def crew(self, value: list[Crew]):
        """Set the list of crew members on the flight."""
        pass
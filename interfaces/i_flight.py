from abc import ABC, abstractmethod

class I_Flight(ABC):
    @abstractmethod
    def get_flight_by_id(self, flight_id: int):
        """Retrieve a flight by its ID."""
        pass

    @abstractmethod
    def get_flights_by_destination(self, destination: str):
        """Retrieve flights by their destination."""
        pass

    @abstractmethod
    def create_flight(self, flight_data: dict):
        """Create a new flight with the provided data."""
        pass

    @abstractmethod
    def update_flight(self, flight_id: int, flight_data: dict):
        """Update an existing flight's information."""
        pass

    @abstractmethod
    def delete_flight(self, flight_id: int):
        """Delete a flight by its ID."""
        pass
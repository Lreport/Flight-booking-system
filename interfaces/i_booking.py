from abc import ABC, abstractmethod

class i_Booking(ABC):
    @abstractmethod
    def get_booking_by_id(self, booking_id: int):
        """Retrieve a booking by its ID."""
        pass

    @abstractmethod
    def get_bookings_by_user_id(self, user_id: int):
        """Retrieve bookings associated with a specific user ID."""
        pass

    @abstractmethod
    def create_booking(self, booking_data: dict):
        """Create a new booking with the provided data."""
        pass

    @abstractmethod
    def update_booking(self, booking_id: int, booking_data: dict):
        """Update an existing booking's information."""
        pass

    @abstractmethod
    def delete_booking(self, booking_id: int):
        """Delete a booking by its ID."""
        pass
from typing import TYPE_CHECKING
from models.user import User

if TYPE_CHECKING:
    from models.contact import Contact

class Passenger(User):
    def __init__(self, id_user: int, name: str, contact=None):
        super().__init__(id_user, name, contact)
        self._assigned_seat = None

    @property
    def assigned_seat(self):
        return self._assigned_seat

    @assigned_seat.setter
    def assigned_seat(self, value):
        self._assigned_seat = value

    def cancel_booking(self):
        """Cancela a reserva do passageiro"""
        if self._assigned_seat:
            self._assigned_seat.passenger = None
            self._assigned_seat = None

    def book_ticket(self, flight, seat_id: int):
        """Reserva um assento em um voo específico"""
        flight.add_passenger(self, seat_id)
        self._assigned_seat = flight.seats[seat_id - 1]

    def __str__(self):
        return f"Passageiro: {self.name} (ID: {self.id_user})"

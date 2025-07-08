from typing import TYPE_CHECKING, Optional
from models.user import User
from interfaces.Ipassenger import Ipassenger

if TYPE_CHECKING:
    from models.contact import Contact
    from models.seat import Seat

class Passenger(User, Ipassenger):
    def __init__(self, id_user: int, name: str, contact=None):
        super().__init__(id_user, name, contact)
        self._assigned_seat = None

    @property
    def assigned_seat(self) -> Optional['Seat']:
        return self._assigned_seat

    @assigned_seat.setter
    def assigned_seat(self, value: Optional['Seat']):
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

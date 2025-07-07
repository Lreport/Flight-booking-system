from typing import TYPE_CHECKING
from interfaces.Ipassenger import IPassenger

if TYPE_CHECKING:
    from models.contact import Contact
    from models.user import User

class Passenger(IPassenger):
    def __init__(self, id_user: int, first_name: str, last_name: str, contact: 'Contact' = None):
        self._id_user       = id_user
        self._first_name    = first_name
        self._last_name     = last_name
        self._contact       = contact
        self._assigned_seat = None

    @property
    def id_user(self):
        return self._id_user

    @id_user.setter
    def id_user(self, value):
        self._id_user = value

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = value

    @property
    def contact(self):
        return self._contact

    @contact.setter
    def contact(self, value):
        self._contact = value

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
        return f"Passageiro: {self.first_name} {self.last_name} (ID: {self.id_user})"
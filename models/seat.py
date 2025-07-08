from typing import TYPE_CHECKING, Optional
from interfaces.Iseat import Iseat

if TYPE_CHECKING:
    from models.flight import Flight
    from models.passenger import Passenger

class Seat(Iseat):
    def __init__(self, id_seat:int, flight:'Flight', passenger:Optional['Passenger']):
        self._id_seat       = id_seat
        self._flight        = flight
        self._passenger     = passenger

    @property
    def id_seat(self):
        return self._id_seat

    @id_seat.setter
    def id_seat(self, value):
        self._id_seat = value

    @property
    def flight(self):
        return self._flight

    @flight.setter
    def flight(self, value):
        self._flight = value

    @property
    def passenger(self):
        return self._passenger

    @passenger.setter
    def passenger(self, value: Optional['Passenger']):
        self._passenger = value

    def is_occupied(self):
        """Verifica se o assento está ocupado"""
        return self._passenger is not None

    def __str__(self):
        status = "Ocupado" if self.is_occupied() else "Livre"
        passenger_name = f" - {self._passenger.name}" if self._passenger else ""
        return f"Assento {self._id_seat} ({status}){passenger_name}"

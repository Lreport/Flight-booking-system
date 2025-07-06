from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.flight import Flight
    from models.passenger import Passenger

class Seat:
    def __init__(self, id_seat:int, flight:Flight, passenger:Passenger):
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
    def passenger(self, value):
        self._passenger = value

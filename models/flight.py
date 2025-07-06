from typing import List
from models.passenger import Passenger
from models.crew import Crew


class Flight:
    def __init__(self, id_flight:int, flight_number:str, origin:str, destination:str, departure_time:str, arrival_time:str, price:float ):
        self._id_flight      = id_flight
        self._flight_number  = flight_number
        self._origin         = origin
        self._destination    = destination
        self._departure_time = departure_time
        self._arrival_time   = arrival_time
        self._price          = price

        self._passengers: List[Passenger] = []
        self._crew: List[Crew] = []

    @property
    def id_flight(self):
        return self._id_flight

    @id_flight.setter
    def id_flight(self, value):
        self._id_flight = value

    @property
    def flight_number(self):
        return self._flight_number

    @flight_number.setter
    def flight_number(self, value):
        self._flight_number = value

    @property
    def origin(self):
        return self._origin

    @origin.setter
    def origin(self, value):
        self._origin = value

    @property
    def destination(self):
        return self._destination

    @destination.setter
    def destination(self, value):
        self._destination = value

    @property
    def departure_time(self):
        return self._departure_time

    @departure_time.setter
    def departure_time(self, value):
        self._departure_time = value

    @property
    def arrival_time(self):
        return self._arrival_time

    @arrival_time.setter
    def arrival_time(self, value):
        self._arrival_time = value

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        self._price = value

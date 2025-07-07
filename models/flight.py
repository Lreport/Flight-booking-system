from typing import List
from models.passenger import Passenger
from models.crew import Crew
from models.seat import Seat
from interfaces.Iflight import IFlight


class Flight(IFlight):
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
        self._seats: List[Seat] = []
        
        # Criar 250 assentos para o voo
        self._create_seats()

    def _create_seats(self):
        """Cria 250 assentos para o voo"""
        for i in range(1, 251):
            seat = Seat(i, self, None)  # Inicialmente sem passageiro
            self._seats.append(seat)

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

    @property
    def passengers(self):
        return self._passengers

    @passengers.setter
    def passengers(self, value):
        self._passengers = value

    @property
    def crew(self):
        return self._crew

    @crew.setter
    def crew(self, value):
        self._crew = value

    @property
    def seats(self):
        return self._seats

    def add_passenger(self, passenger: Passenger, seat_id: int):
        """Adiciona um passageiro a um assento específico"""
        if seat_id < 1 or seat_id > 250:
            raise ValueError("ID do assento deve estar entre 1 e 250")
        
        seat = self._seats[seat_id - 1]  # Assentos começam do índice 0
        if seat.passenger is not None:
            raise ValueError(f"Assento {seat_id} já está ocupado")
        
        seat.passenger = passenger
        if passenger not in self._passengers:
            self._passengers.append(passenger)

    def add_crew_member(self, crew_member: Crew):
        """Adiciona um membro da tripulação ao voo"""
        if crew_member not in self._crew:
            self._crew.append(crew_member)

    def get_available_seats(self):
        """Retorna lista de assentos disponíveis"""
        return [seat for seat in self._seats if seat.passenger is None]

    def get_occupied_seats(self):
        """Retorna lista de assentos ocupados"""
        return [seat for seat in self._seats if seat.passenger is not None]

    def get_random_seats(self, count: int = 10):
        """Retorna uma lista de assentos aleatórios"""
        import random
        return random.sample(self._seats, min(count, len(self._seats)))

    def __str__(self):
        return f"Voo {self._flight_number}: {self._origin} → {self._destination} (R$ {self._price:.2f})"

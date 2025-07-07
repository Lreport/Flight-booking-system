from typing import List
from typing import Optional
from models.flight import Flight
from models.passenger import Passenger
from models.crew import Pilot, Copilot, Commissar
from utils.nameGenerate import name_generate
import random


class FlightController:
    def __init__(self):
        self._flights: List[Flight] = []
        self._initialize_system()

    def _initialize_system(self):
        self._create_flights_and_fill()
        self._create_and_assign_crew()

    def _create_flights_and_fill(self):
        flight_data = [
            (1, "AA101", "São Paulo", "Rio de Janeiro", "08:00", "09:30", 450.00),
            (2, "AA102", "Rio de Janeiro", "Brasília", "10:00", "11:45", 380.00),
            (3, "AA103", "Brasília", "Salvador", "14:00", "16:15", 520.00),
            (4, "AA104", "Salvador", "Recife", "09:30", "11:00", 290.00),
            (5, "AA105", "Recife", "Fortaleza", "13:00", "14:30", 340.00),
            (6, "AA106", "Fortaleza", "Manaus", "16:00", "19:30", 780.00),
            (7, "AA107", "Manaus", "Porto Alegre", "07:00", "11:45", 920.00),
            (8, "AA108", "Porto Alegre", "Curitiba", "15:00", "16:15", 310.00),
            (9, "AA109", "Curitiba", "Belo Horizonte", "12:00", "13:30", 420.00),
            (10, "AA110", "Belo Horizonte", "São Paulo", "18:00", "19:15", 360.00)
        ]
        passenger_names = name_generate(2500)
        name_idx = 0
        for flight_info in flight_data:
            flight = Flight(*flight_info)
            for seat_id in range(1, 251):
                name = passenger_names[name_idx]
                name_idx += 1
                passenger = Passenger(seat_id, name)
                flight.add_passenger(passenger, seat_id)
            self._flights.append(flight)

    def _create_and_assign_crew(self):
        crew_names = name_generate(30)
        for i, flight in enumerate(self._flights):
            pilot = Pilot(1000 + i, crew_names[i])
            copilot = Copilot(2000 + i, crew_names[i+10])
            commissar = Commissar(3000 + i, crew_names[i+20])
            flight.add_crew_member(pilot)
            flight.add_crew_member(copilot)
            flight.add_crew_member(commissar)

    def show_flights_and_random_seats(self):
        print("=" * 80)
        print("SISTEMA DE RESERVAS DE VOOS")
        print("=" * 80)
        for flight in self._flights:
            print(f"\n{flight}")
            print(f"Horário: {flight.departure_time} - {flight.arrival_time}")
            print(f"Passageiros: 250/250")
            print(f"Tripulação: 3 membros")
            random_seats = flight.get_random_seats(10)
            print("10 Assentos Aleatórios (todos ocupados):")
            for seat in random_seats:
                print(f"  Assento {seat.id_seat}: {seat.passenger.name}")
            print("-" * 60)

    def show_crew_by_flight(self):
        print("\n" + "=" * 80)
        print("TRIPULAÇÃO POR VOO")
        print("=" * 80)
        for flight in self._flights:
            print(f"\n{flight}")
            print("Tripulação:")
            for crew_member in flight.crew:
                print(f"  {crew_member.role}: {crew_member.name}")
            print("-" * 60)

    def get_all_flights(self) -> List[Flight]:
        """Retorna todos os voos"""
        return self._flights

    def get_flight_by_id(self, flight_id: int) -> Optional[Flight]:
        """Retorna um voo específico por ID"""
        for flight in self._flights:
            if flight.id_flight == flight_id:
                return flight
        return None

    def get_system_summary(self):
        """Retorna um resumo do sistema"""
        total_passengers = sum(len(flight.passengers) for flight in self._flights)
        total_crew = sum(len(flight.crew) for flight in self._flights)
        total_seats = len(self._flights) * 250
        
        return {
            "total_flights": len(self._flights),
            "total_passengers": total_passengers,
            "total_crew": total_crew,
            "total_seats": total_seats,
            "available_seats": total_seats - total_passengers
        } 
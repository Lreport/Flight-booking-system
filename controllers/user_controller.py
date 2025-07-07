from models.passenger import Passenger
from models.crew import Crew, Pilot, Copilot, Commissar
from utils.nameGenerate import name_generate

class UserController:
    def __init__(self, num_flights=10, seats_per_flight=250):
        self.num_flights = num_flights
        self.seats_per_flight = seats_per_flight
        self.total_users = num_flights * (seats_per_flight + 3)  # 3 tripulantes por voo
        self.users = []
        self.passengers = []
        self.crew_by_flight = []  # Lista de listas: cada sublista = [pilot, copilot, commissar]
        self._generate_users()

    def _generate_users(self):
        names = name_generate()
        assert len(names) >= self.total_users, "Faker não gerou nomes suficientes."
        user_id = 1
        name_idx = 0
        # Para cada voo, criar 3 tripulantes e 250 passageiros
        for flight_idx in range(self.num_flights):
            # Tripulação
            pilot_name = names[name_idx].split()
            pilot = Pilot(user_id, pilot_name[0], " ".join(pilot_name[1:]) or "Sobrenome", None)
            user_id += 1
            name_idx += 1
            copilot_name = names[name_idx].split()
            copilot = Copilot(user_id, copilot_name[0], " ".join(copilot_name[1:]) or "Sobrenome", None)
            user_id += 1
            name_idx += 1
            commissar_name = names[name_idx].split()
            commissar = Commissar(user_id, commissar_name[0], " ".join(commissar_name[1:]) or "Sobrenome", None)
            user_id += 1
            name_idx += 1
            self.crew_by_flight.append([pilot, copilot, commissar])
            self.users.extend([pilot, copilot, commissar])
            # Passageiros
            for _ in range(self.seats_per_flight):
                passenger_name = names[name_idx].split()
                passenger = Passenger(user_id, passenger_name[0], " ".join(passenger_name[1:]) or "Sobrenome", None)
                self.passengers.append(passenger)
                self.users.append(passenger)
                user_id += 1
                name_idx += 1

    def get_crew_for_flight(self, flight_idx):
        return self.crew_by_flight[flight_idx]

    def get_passengers_for_flight(self, flight_idx):
        start = flight_idx * self.seats_per_flight
        end = start + self.seats_per_flight
        return self.passengers[start:end]

    def get_all_users(self):
        return self.users

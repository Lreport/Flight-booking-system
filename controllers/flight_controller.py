from typing import List
from models.flight import Flight
from models.passenger import Passenger
from models.crew import Crew, Pilot, Copilot, Commissar
from models.contact import Contact
from models.address import Address
from utils.nameGenerate import name_generate
import random


class FlightController:
    def __init__(self):
        self._flights: List[Flight] = []
        self._passengers: List[Passenger] = []
        self._crew_members: List[Crew] = []
        self._initialize_system()

    def _initialize_system(self):
        """Inicializa o sistema com 10 voos, passageiros e tripulação"""
        self._create_flights()
        self._create_passengers()
        self._create_crew_members()
        self._assign_passengers_to_flights()
        self._assign_crew_to_flights()

    def _create_flights(self):
        """Cria 10 voos com preços diferentes"""
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

        for flight_info in flight_data:
            flight = Flight(*flight_info)
            self._flights.append(flight)

    def _create_passengers(self):
        """Cria passageiros usando o gerador de nomes"""
        names = name_generate()
        
        for i, name in enumerate(names, 1):
            # Criar dados de contato fictícios
            address = Address(
                i,  # id_address
                f"Rua {random.randint(1, 100)}",  # street
                f"Cidade {random.randint(1, 10)}",  # city
                f"Estado {random.randint(1, 27)}",  # state
                "Brasil",  # country
                f"{random.randint(10000, 99999)}-{random.randint(100, 999)}"  # zip_code
            )
            
            contact = Contact(
                i,  # id_contact
                address,  # address
                address._id_address,  # id_address
                f"passenger{i}@email.com",  # email
                f"+55{random.randint(100000000, 999999999)}"  # phone_number
            )
            
            # Dividir o nome em primeiro e último nome
            name_parts = name.split()
            first_name = name_parts[0] if name_parts else "Nome"
            last_name = " ".join(name_parts[1:]) if len(name_parts) > 1 else "Sobrenome"
            
            passenger = Passenger(i, first_name, last_name, contact)
            self._passengers.append(passenger)

    def _create_crew_members(self):
        """Cria membros da tripulação"""
        crew_names = [
            ("João Silva", "Pilot"),
            ("Maria Santos", "Copilot"),
            ("Pedro Oliveira", "Pilot"),
            ("Ana Costa", "Copilot"),
            ("Carlos Ferreira", "Pilot"),
            ("Lucia Rodrigues", "Copilot"),
            ("Roberto Almeida", "Pilot"),
            ("Fernanda Lima", "Copilot"),
            ("Marcos Pereira", "Pilot"),
            ("Juliana Souza", "Copilot"),
            ("Ricardo Martins", "Commissar"),
            ("Patricia Gomes", "Commissar"),
            ("Andre Silva", "Commissar"),
            ("Camila Santos", "Commissar"),
            ("Diego Oliveira", "Commissar"),
            ("Vanessa Costa", "Commissar"),
            ("Thiago Ferreira", "Commissar"),
            ("Amanda Rodrigues", "Commissar"),
            ("Bruno Almeida", "Commissar"),
            ("Carolina Lima", "Commissar")
        ]

        for i, (name, role) in enumerate(crew_names, 1):
            # Criar dados de contato fictícios
            address = Address(
                i + 10000,  # id_address
                f"Rua {random.randint(1, 100)}",  # street
                f"Cidade {random.randint(1, 10)}",  # city
                f"Estado {random.randint(1, 27)}",  # state
                "Brasil",  # country
                f"{random.randint(10000, 99999)}-{random.randint(100, 999)}"  # zip_code
            )
            
            contact = Contact(
                i + 10000,  # id_contact
                address,  # address
                address._id_address,  # id_address
                f"crew{i}@airline.com",  # email
                f"+55{random.randint(100000000, 999999999)}"  # phone_number
            )
            
            name_parts = name.split()
            first_name = name_parts[0]
            last_name = " ".join(name_parts[1:])
            
            if role == "Pilot":
                crew_member = Pilot(i + 1000, first_name, last_name, contact)
            elif role == "Copilot":
                crew_member = Copilot(i + 1000, first_name, last_name, contact)
            else:
                crew_member = Commissar(i + 1000, first_name, last_name, contact)
            
            self._crew_members.append(crew_member)

    def _assign_passengers_to_flights(self):
        """Associa passageiros aleatoriamente aos voos"""
        for passenger in self._passengers:
            # Escolher um voo aleatório
            flight = random.choice(self._flights)
            
            # Encontrar um assento disponível
            available_seats = flight.get_available_seats()
            if available_seats:
                seat = random.choice(available_seats)
                seat.passenger = passenger
                passenger.assigned_seat = seat
                if passenger not in flight.passengers:
                    flight.passengers.append(passenger)

    def _assign_crew_to_flights(self):
        """Associa tripulação aos voos"""
        pilots = [crew for crew in self._crew_members if isinstance(crew, Pilot)]
        copilots = [crew for crew in self._crew_members if isinstance(crew, Copilot)]
        commissars = [crew for crew in self._crew_members if isinstance(crew, Commissar)]

        for i, flight in enumerate(self._flights):
            # Cada voo tem 1 piloto, 1 copiloto e 2 comissários
            if i < len(pilots):
                flight.add_crew_member(pilots[i])
            if i < len(copilots):
                flight.add_crew_member(copilots[i])
            
            # Adicionar comissários (2 por voo)
            commissar_indices = [i * 2, i * 2 + 1]
            for idx in commissar_indices:
                if idx < len(commissars):
                    flight.add_crew_member(commissars[idx])

    def get_all_flights(self) -> List[Flight]:
        """Retorna todos os voos"""
        return self._flights

    def get_flight_by_id(self, flight_id: int) -> Flight:
        """Retorna um voo específico por ID"""
        for flight in self._flights:
            if flight.id_flight == flight_id:
                return flight
        return None

    def show_flights_and_random_seats(self):
        """Mostra todos os voos e 10 assentos aleatórios de cada um"""
        print("=" * 80)
        print("SISTEMA DE RESERVAS DE VOOS")
        print("=" * 80)
        
        for flight in self._flights:
            print(f"\n{flight}")
            print(f"Horário: {flight.departure_time} - {flight.arrival_time}")
            print(f"Passageiros: {len(flight.passengers)}/250")
            print(f"Tripulação: {len(flight.crew)} membros")
            
            # Mostrar 10 assentos aleatórios
            random_seats = flight.get_random_seats(10)
            print("10 Assentos Aleatórios:")
            for seat in random_seats:
                print(f"  {seat}")
            print("-" * 60)

    def show_crew_by_flight(self):
        """Mostra a tripulação de cada voo"""
        print("\n" + "=" * 80)
        print("TRIPULAÇÃO POR VOO")
        print("=" * 80)
        
        for flight in self._flights:
            print(f"\n{flight}")
            print("Tripulação:")
            for crew_member in flight.crew:
                print(f"  {crew_member}")
            print("-" * 60)

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
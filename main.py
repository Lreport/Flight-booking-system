from controllers.flight_controller import FlightController
from faker import Faker

def main():
    print("Inicializando Sistema de Reservas de Voos...")
    print("=" * 50)
    
    flight_controller = FlightController()
    
    # Mostrar voos e assentos aleatórios
    flight_controller.show_flights_and_random_seats()
    
    # Mostrar tripulação por voo
    flight_controller.show_crew_by_flight()
    
    print("\n" + "=" * 50)
    print("SISTEMA EXECUTADO COM SUCESSO!")
    print("=" * 50)

if __name__ == "__main__":
    main()
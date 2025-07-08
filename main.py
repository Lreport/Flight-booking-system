from controllers.flight_controller import FlightController

def main():
    print("Inicializando Sistema de Reservas de Voos...")
    print("=" * 50)
    
    flight_controller = FlightController()
    
    flight_controller.show_flights_and_random_seats()
    
    flight_controller.show_crew_by_flight()
    
    print("\n" + "=" * 50)
    print("SISTEMA EXECUTADO COM SUCESSO!")
    print("=" * 50)

if __name__ == "__main__":
    main()
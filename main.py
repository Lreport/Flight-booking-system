from controllers.flight_controller import FlightController

def main():
    print("Inicializando Sistema de Reservas de Voos...")
    print("=" * 50)
    
    # Criar o controlador do sistema
    flight_controller = FlightController()
    
    # Mostrar resumo do sistema
    summary = flight_controller.get_system_summary()
    print(f"\nRESUMO DO SISTEMA:")
    print(f"Total de voos: {summary['total_flights']}")
    print(f"Total de passageiros: {summary['total_passengers']}")
    print(f"Total de tripulação: {summary['total_crew']}")
    print(f"Total de assentos: {summary['total_seats']}")
    print(f"Assentos disponíveis: {summary['available_seats']}")
    
    # Mostrar voos e assentos aleatórios
    flight_controller.show_flights_and_random_seats()
    
    # Mostrar tripulação por voo
    flight_controller.show_crew_by_flight()
    
    print("\n" + "=" * 80)
    print("SISTEMA EXECUTADO COM SUCESSO!")
    print("=" * 80)

if __name__ == "__main__":
    main()
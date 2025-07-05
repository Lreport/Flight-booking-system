from datetime import datetime


class Flight:
    def __init__(self, id, price, seats, crew, ):
        self.__idFlight = id
        self.__price = price
        self.__seats = seats
        self.__crew = crew
        self.__status = None
        self.__departureTime = datetime.now()
        self.__arrivalTime = datetime.now()

    @property
    def _idFlight(self):
        return self.__idFlight

    @_idFlight.setter
    def _idFlight(self, value):
        self.__idFlight = value

    @property
    def _price(self):
        return self.__price

    @_price.setter
    def _price(self, value):
        self.__price = value

    @property
    def _seats(self):
        return self.__seats

    @_seats.setter
    def _seats(self, value):
        self.__seats = value

    @property
    def _crew(self):
        return self.__crew

    @_crew.setter
    def _crew(self, value):
        self.__crew = value

    @property
    def _status(self):
        return self.__status

    @_status.setter
    def _status(self, value):
        self.__status = value

    @property
    def _departureTime(self):
        return self.__departureTime

    @_departureTime.setter
    def _departureTime(self, value):
        self.__departureTime = value

    @property
    def _arrivalTime(self):
        return self.__arrivalTime

    @_arrivalTime.setter
    def _arrivalTime(self, value):
        self.__arrivalTime = value


from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.Flight import Flight
    from models.User import User

class Booking:
    def __init__(self, id:int, userId: User, bookingNum:str, bookingDate: str, travelDate:str, totalCost: float, flightBooked: Flight):
        self.__idBooking = id
        self.__userId = userId
        self.__bookingNum = bookingNum
        self.__bookingDate = bookingDate
        self.__travelDate = travelDate
        self.__totalCost = totalCost
        self.__flightBooked = flightBooked

    @property
    def _idBooking(self):
        return self.__idBooking

    @_idBooking.setter
    def _idBooking(self, value):
        self.__idBooking = value

    @property
    def _userId(self):
        return self.__userId

    @_userId.setter
    def _userId(self, value):
        self.__userId = value

    @property
    def _bookingNum(self):
        return self.__bookingNum

    @_bookingNum.setter
    def _bookingNum(self, value):
        self.__bookingNum = value

    @property
    def _bookingDate(self):
        return self.__bookingDate

    @_bookingDate.setter
    def _bookingDate(self, value):
        self.__bookingDate = value

    @property
    def _travelDate(self):
        return self.__travelDate

    @_travelDate.setter
    def _travelDate(self, value):
        self.__travelDate = value

    @property
    def _totalCost(self):
        return self.__totalCost

    @_totalCost.setter
    def _totalCost(self, value):
        self.__totalCost = value

    @property
    def _flightBooked(self):
        return self.__flightBooked

    @_flightBooked.setter
    def _flightBooked(self, value):
        self.__flightBooked = value




:
#fazer a classe payment para posteriormente criar o metodo de pagamento
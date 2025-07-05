from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.Booking import Booking



class Payment:
    def __init__(self, payment_id: int, booking_id: Booking, amount: float, payment_method: str, payment_date: str):
        self.__payment_id = payment_id
        self.__booking_id = booking_id
        self.__amount = amount
        self.__payment_method = payment_method
        self.__payment_date = payment_date

    @property
    def _payment_id(self):
        return self.__payment_id

    @_payment_id.setter
    def _payment_id(self, value):
        self.__payment_id = value

    @property
    def _booking_id(self):
        return self.__booking_id

    @_booking_id.setter
    def _booking_id(self, value):
        self.__booking_id = value

    @property
    def _amount(self):
        return self.__amount

    @_amount.setter
    def _amount(self, value):
        self.__amount = value

    @property
    def _payment_method(self):
        return self.__payment_method

    @_payment_method.setter
    def _payment_method(self, value):
        self.__payment_method = value

    @property
    def _payment_date(self):
        return self.__payment_date

    @_payment_date.setter
    def _payment_date(self, value):
        self.__payment_date = value

from typing import Optional
from interfaces.Iaddress import Iaddress

class Address(Iaddress):
    def __init__(self, id_address: Optional[int] = None, street: Optional[str] = None, city: Optional[str] = None, state: Optional[str] = None, country: Optional[str] = None, zip_code: Optional[str] = None):
        self._id_address = id_address
        self._street = street
        self._city = city
        self._state = state
        self._country = country
        self._zip_code = zip_code

    @property
    def id_address(self) -> Optional[int]:
        return self._id_address

    @id_address.setter
    def id_address(self, value: Optional[int]):
        self._id_address = value

    @property
    def street(self) -> Optional[str]:
        return self._street

    @street.setter
    def street(self, value: Optional[str]):
        self._street = value

    @property
    def city(self) -> Optional[str]:
        return self._city

    @city.setter
    def city(self, value: Optional[str]):
        self._city = value

    @property
    def state(self) -> Optional[str]:
        return self._state

    @state.setter
    def state(self, value: Optional[str]):
        self._state = value

    @property
    def country(self) -> Optional[str]:
        return self._country

    @country.setter
    def country(self, value: Optional[str]):
        self._country = value

    @property
    def zip_code(self) -> Optional[str]:
        return self._zip_code

    @zip_code.setter
    def zip_code(self, value: Optional[str]):
        self._zip_code = value

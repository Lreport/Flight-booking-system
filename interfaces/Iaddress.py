from abc import ABC, abstractmethod
from typing import Optional

class Iaddress(ABC):
    #########################################################
    @property
    @abstractmethod
    def id_address(self) -> Optional[int]:
        """Get the address ID."""
        pass

    @id_address.setter
    @abstractmethod
    def id_address(self, value: Optional[int]):
        """Set the address ID."""
        pass

    #########################################################
    @property
    @abstractmethod
    def street(self) -> Optional[str]:
        """Get the street name."""
        pass

    @street.setter
    @abstractmethod
    def street(self, value: Optional[str]):
        """Set the street name."""
        pass

    #########################################################
    @property
    @abstractmethod
    def city(self) -> Optional[str]:
        """Get the city name."""
        pass

    @city.setter
    @abstractmethod
    def city(self, value: Optional[str]):
        """Set the city name."""
        pass

    #########################################################
    @property
    @abstractmethod
    def state(self) -> Optional[str]:
        """Get the state name."""
        pass

    @state.setter
    @abstractmethod
    def state(self, value: Optional[str]):
        """Set the state name."""
        pass

    #########################################################
    @property
    @abstractmethod
    def country(self) -> Optional[str]:
        """Get the country name."""
        pass

    @country.setter
    @abstractmethod
    def country(self, value: Optional[str]):
        """Set the country name."""
        pass

    #########################################################
    @property
    @abstractmethod
    def zip_code(self) -> Optional[str]:
        """Get the zip code."""
        pass

    @zip_code.setter
    @abstractmethod
    def zip_code(self, value: Optional[str]):
        """Set the zip code."""
        pass

    
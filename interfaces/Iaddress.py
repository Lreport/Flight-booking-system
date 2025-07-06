from abc import ABC, abstractmethod

class Iaddress(ABC):
    #########################################################
    @property
    @abstractmethod
    def id_address(self) -> int:
        """Get the address ID."""
        pass

    @id_address.setter
    @abstractmethod
    def id_address(self, value: int):
        """Set the address ID."""
        pass

    #########################################################
    @property
    @abstractmethod
    def street(self) -> str:
        """Get the street name."""
        pass

    @street.setter
    @abstractmethod
    def street(self, value: str):
        """Set the street name."""
        pass

    #########################################################
    @property
    @abstractmethod
    def city(self) -> str:
        """Get the city name."""
        pass

    @city.setter
    @abstractmethod
    def city(self, value: str):
        """Set the city name."""
        pass

    #########################################################
    @property
    @abstractmethod
    def state(self) -> str:
        """Get the state name."""
        pass

    @state.setter
    @abstractmethod
    def state(self, value: str):
        """Set the state name."""
        pass

    #########################################################
    @property
    @abstractmethod
    def country(self) -> str:
        """Get the country name."""
        pass

    @country.setter
    @abstractmethod
    def country(self, value: str):
        """Set the country name."""
        pass

    #########################################################
    @property
    @abstractmethod
    def zip_code(self) -> str:
        """Get the zip code."""
        pass

    @zip_code.setter
    @abstractmethod
    def zip_code(self, value: str):
        """Set the zip code."""
        pass

    
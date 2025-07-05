from abc import ABC, abstractmethod

class I_Address(ABC):
    @abstractmethod
    def get_address_by_id(self, address_id: int):
        """Retrieve an address by its ID."""
        pass

    @abstractmethod
    def get_addresses_by_user_id(self, user_id: int):
        """Retrieve addresses associated with a specific user ID."""
        pass

    @abstractmethod
    def create_address(self, address_data: dict):
        """Create a new address with the provided data."""
        pass

    @abstractmethod
    def update_address(self, address_id: int, address_data: dict):
        """Update an existing address's information."""
        pass

    @abstractmethod
    def delete_address(self, address_id: int):
        """Delete an address by its ID."""
        pass
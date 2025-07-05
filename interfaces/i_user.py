from abc import ABC, abstractmethod

class I_User(ABC):
    @abstractmethod
    def get_user_by_id(self, user_id: int):
        """Retrieve a user by their ID."""
        pass

    @abstractmethod
    def get_user_by_username(self, username: str):
        """Retrieve a user by their username."""
        pass

    @abstractmethod
    def create_user(self, user_data: dict):
        """Create a new user with the provided data."""
        pass

    @abstractmethod
    def update_user(self, user_id: int, user_data: dict):
        """Update an existing user's information."""
        pass

    @abstractmethod
    def delete_user(self, user_id: int):
        """Delete a user by their ID."""
        pass
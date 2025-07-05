from abc import ABC, abstractmethod

class I_Contact(ABC):
    @abstractmethod
    def get_contact_by_id(self, contact_id: int):
        """Retrieve a contact by its ID."""
        pass

    @abstractmethod
    def get_contacts_by_user_id(self, user_id: int):
        """Retrieve contacts associated with a specific user ID."""
        pass

    @abstractmethod
    def create_contact(self, contact_data: dict):
        """Create a new contact with the provided data."""
        pass

    @abstractmethod
    def update_contact(self, contact_id: int, contact_data: dict):
        """Update an existing contact's information."""
        pass

    @abstractmethod
    def delete_contact(self, contact_id: int):
        """Delete a contact by its ID."""
        pass    
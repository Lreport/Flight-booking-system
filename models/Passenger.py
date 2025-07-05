from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.contact import Contact
    from models.user import User

class Passenger(User):
    def __init__(self, id_user: int, first_name: str, last_name: str, email: str, phone: str, contact: 'Contact'):
        super().__init__(id_user, first_name, last_name, email, phone, contact)
        self._id_passenger = id_user 

    @property
    def id_passenger(self):
        return self._id_passenger

    @id_passenger.setter
    def id_passenger(self, value):
        self._id_passenger = value


from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.contact import Contact
    from models.user import User

class Passenger(User):
    def __init__(self, id_user: int, first_name: str, last_name: str, contact: 'Contact'): #interessante colar genero para caso seja mulher ter a opção gestante.
        super().__init__(id_user, first_name, last_name, contact)
        # sem necessidade de id específico para passageiro, pois é igual ao id do usuário


    def cancel_booking(self):
        pass

    def book_ticket(self):
        pass
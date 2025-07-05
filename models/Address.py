class Address:
    def __init__(self, id_address:int, street:str, city:str, state:str, country:str, zip_code:str):
        self._id_address = id_address
        self._street = street
        self._city = city
        self._state = state
        self._country = country
        self._zip_code = zip_code

    @property
    def id_address(self):
        return self._id_address

    @id_address.setter
    def id_address(self, value):
        self._id_address = value

    @property
    def street(self):
        return self._street

    @street.setter
    def street(self, value):
        self._street = value

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, value):
        self._country = value

    @property
    def zip_code(self):
        return self._zip_code

    @zip_code.setter
    def zip_code(self, value):
        self._zip_code = value

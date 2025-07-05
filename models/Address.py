class Address:
    def __init__(self, id: int, type:str, addressNum:str, zipCode:str, city:str, state:str, country:str):
        self.__idContact = id
        self.__type = type
        self.__addressNum = addressNum
        self.__zipCode = zipCode
        self.__city = city
        self.__state = state
        self.__country = country

    @property
    def _idContact(self):
        return self.__idContact

    @_idContact.setter
    def _idContact(self, value):
        self.__idContact = value

    @property
    def _type(self):
        return self.__type

    @_type.setter
    def _type(self, value):
        self.__type = value

    @property
    def _addressNum(self):
        return self.__addressNum

    @_addressNum.setter
    def _addressNum(self, value):
        self.__addressNum = value

    @property
    def _zipCode(self):
        return self.__zipCode

    @_zipCode.setter
    def _zipCode(self, value):
        self.__zipCode = value

    @property
    def _city(self):
        return self.__city

    @_city.setter
    def _city(self, value):
        self.__city = value

    @property
    def _state(self):
        return self.__state

    @_state.setter
    def _state(self, value):
        self.__state = value

    @property
    def _country(self):
        return self.__country

    @_country.setter
    def _country(self, value):
        self.__country = value




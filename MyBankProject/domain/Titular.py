from domain.Person import Person


class Titular(Person):

    def __init__(self, id, name, last_name, mail, phone, product, key):
        super().__init__( id, name, last_name, mail, phone)
        self.__product = product
        self.__key = key

    @property
    def product(self):
        return self.__product

    @product.setter
    def product(self, product):
        self.__product = product

    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, key):
        self.__key



    def create_person(self, product):
        super().create_person()
        value = int((input("Seleccione 1. Ahorro 2. Credito")))
        self.__product = product.products[value]
        self.__key = int(input("Key"))
        self.users[self._id] = self.name, self.last_name, self.mail, self.phone, self.key,self.product

    def __str__(self, product):
        print= f"""
        {super().__str__()}
        producto: {self.__product},
        key: {self.__key}

        """
        return print

    def select_user(self):
        for i in self.users.items():
            print(i)
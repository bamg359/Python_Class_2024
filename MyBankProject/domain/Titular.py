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
        self.__product = product.product_name
        self.__key = int(input("Key"))

    def __str__(self, product):
        print= f"""
        {super().__str__()}
        producto: {self.__product},
        key: {self.__key}

        """
        return print
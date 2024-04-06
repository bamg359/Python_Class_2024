

class Product:

    def __init__(self, id_product, product_name):
        self.__id_product = 1
        self.__product_name = "Cuenta Ahorro"


    @property
    def product_name(self):
        return self.__product_name
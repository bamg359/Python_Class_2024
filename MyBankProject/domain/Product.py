

class Product:

    def __init__(self, id_product, product_name):
        self.__id_product = id_product
        self.__product_name = product_name

    @property
    def product_name(self):
        return self.__product_name

    @product_name.setter
    def product_name(self, product_name):
        self.__product_name = product_name

    @property
    def id_product(self):
        return self.__id_product


    @id_product.setter
    def id_product(self, id_product):
        self.__id_product = id_product

    products = {}




    def create_product(self):
        self.__id_product = int(input("Product Id: "))
        self.__product_name = input("Product Name: ")
        self.products[self.__id_product]= self.__product_name


    def select_product(self):
        for i in self.products.items():
            print(i)
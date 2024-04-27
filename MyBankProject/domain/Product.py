

class Product:

    def __init__(self, id_product, product_name):
        self.__id_product = id_product
        self.product_name = product_name

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

    @staticmethod
    def from_row(row):
        return Product(row[0],row[1])

    def create_product(self):
        #self.__id_product = int(input("Product Id: "))
        self.__product_name = input("Product Name: ")
        print(type(self.product_name))
        #self.products[self.__id_product]= self.__product_name


    def insert_product(self, db):
        query = "INSERT INTO producto (nombre_producto) values(%s)"
        values= ( self.__product_name,)
        db.execute_query(query,values)


    @staticmethod
    def select_product( db, id_product):
        query = "SELECT * fROM producto WHERE id_producto = %s"
        result = db.execute_query(query,(id_product,))
        if result:
            return Product.from_row(result[0])
        else:
            print("Producto no encontrado.")
            return None

    def delete_producto(self, db, id_product):
        query = "DELETE FROM producto WHERE id_producto = %s"
        db.execute_query(query, (id_product,))




    """def select_product(self):
        for i in self.products.items():
            print(i)"""
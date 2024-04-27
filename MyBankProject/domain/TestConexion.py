


from domain.ConexionDataBase import ConexionDataBase

from domain.Product import Product



db = ConexionDataBase(host="localhost", port = 3306, user= "root", passwd = "", database = "mybankdb")

db.connect()


product = Product(None,None)

#product.create_product()
#product.insert_product(db)

valor_devuelto = product.select_product(db, 3 )

print(valor_devuelto)

if valor_devuelto:
    print("id Producto: " , valor_devuelto.id_product)
    print(" Nombre producto: " , valor_devuelto.product_name)

product.delete_producto(db, 3)





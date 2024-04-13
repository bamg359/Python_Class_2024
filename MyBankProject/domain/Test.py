from domain.Person import Person
from domain.Product import Product
from domain.Savings_Account import Savings_Account
from domain.Titular import Titular


class Test:

    person = Person(None,None,None
                    ,None,None)

    titular = Titular(None,None, None,None,None,None,None)
    product = Product(None,None)
    account = Savings_Account(123, titular.name,0)



    product.create_product()
    product.create_product()
    product.select_product()
    titular.create_person(product)
    titular.create_person(product)
    #print(titular.__str__(product))
    #account.create_account(titular)
    #print(account.__str__(titular))
    titular.select_user()
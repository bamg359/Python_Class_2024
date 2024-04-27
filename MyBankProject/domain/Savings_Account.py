from domain.Product import Product


class Savings_Account(Product):

    def __init__(self,account_number,product, titular, balance):
        self._bank_id = 46
        self._branch_id = 1
        self._city_id = "05634"
        self._account_number = f"{self._bank_id}{self._branch_id}{self._city_id}{account_number}"
        self.product = product
        self._titular = titular
        self._balance = balance

    def create_account(self, titular, product):
        self.product = product.product_name
        self._titular = titular.name
        self._account_number
        self._balance = int(input("Balance: "))

    def __str__(self, titular):
        print = f"""
        
        titular{self._titular},
        Producto{self.product},
        number{self._account_number}
        balance{self._balance}

        """
        return print
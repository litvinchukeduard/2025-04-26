from collections import UserList
from dataclasses import dataclass
'''
Написати систему, яка буже керувати торговими апаратами
'''

# products = [1]
# products_set = set()

class Product:
    def __init__(self, name: str, price: int):
        self.name = name
        if price <= 0:
            raise ValueError("Price can not be less than or equals to 0")
        self.price = price

    def __str__(self):
        return f"Product(name={self.name}, price={self.price})"

@dataclass(frozen=True)
class DataProduct:
    name: str
    price: int
    ingredients: list

    def __post_init__(self):
        if self.price <= 0:
            raise ValueError("Price can not be less than or equals to 0")


# class VendingMachine(UserList):
class VendingMachine:
    def __init__(self):
        self.products = []

    def add_product(self, product: Product):
        if product in self.products:
            # print("Please check products")
            raise ValueError(f"Please check if product {product.name} is not already in a machine")
        self.products.append(product)

    '''
    Щоб купити продукт, потрібно ввести точну кількість грошей
    '''
    def buy_product(self, name: str, amount_of_money: int):
        result_product = None
        for product in self.products:
            if product.name == name:
                result_product = product

        if result_product.price != amount_of_money:
            raise ValueError('Please enter correct amount of money')
            
        self.products.remove(result_product)
        return result_product


# snickers = Product("Snickers", -10)
data_snicker = DataProduct("Snickers", 10, [1, 2, 3])
# data_snicker.price = 1000
# data_snicker.ingredients.append(4)
print(data_snicker)

# products_set.add(snickers)
# products_set.add(snickers)

# print(snickers)
# products.append(snickers)
# add_product_to_list(snickers)
# add_product_to_list(snickers)
# products.append(snickers)
# print(products_set)
# products = [1]
machine = VendingMachine()
machine.add_product(data_snicker)

machine.buy_product('Snickers', 10)
# machine.add_product(snickers)
# machine.add_product(snickers)

print(machine.products)

# products.append()
# machine.append()

# products[0] = "hello"
# machine[0] = "hello"

# products.append()
# products.insert()
# products[1] = ...

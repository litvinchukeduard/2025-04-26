from collections import UserList
'''
Написати систему, яка буже керувати торговими апаратами
'''

# products = [1]
# products_set = set()

class Product:
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price


# class VendingMachine(UserList):
class VendingMachine:
    def __init__(self):
        self.products = []

    def add_product(self, product: Product):
        if product in self.products:
            # print("Please check products")
            raise ValueError(f"Please check if product {product.name} is not already in a machine")
        self.products.append(product)


snickers = Product("Snickers", 35)

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
machine.add_product(snickers)
machine.add_product(snickers)

print(machine.products)

# products.append()
# machine.append()

# products[0] = "hello"
# machine[0] = "hello"

# products.append()
# products.insert()
# products[1] = ...

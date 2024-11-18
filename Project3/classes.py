class Item:

    def __init__(self, name, unit_price = 1, quantity = 1):
        self._name = name
        self.set_unit_price(unit_price)
        self.set_quantity(quantity)


# UMGPT
# given this class, add set/get methods for quantity and unit price, just a get method for name
#
# class Item:
#
#     def __init__(self, name, unit_price = 1, quantity = 1):
#         self._name = name
#         self._unit_price = unit_price
#         self._quantity = quantity

 # Getter method for name
    def get_name(self):
        return self._name

    # Getter method for unit_price
    def get_unit_price(self):
        return self._unit_price

    # Setter method for unit_price
    def set_unit_price(self, unit_price):
        if unit_price >= 0:
            self._unit_price = unit_price
        else:
            raise ValueError("Unit price must be non-negative")

    # Getter method for quantity
    def get_quantity(self):
        return self._quantity

    # Setter method for quantity
    def set_quantity(self, quantity):
        if quantity >= 0:
            self._quantity = quantity
        else:
            raise ValueError("Quantity must be non-negative")

    def get_total_price(self):
        return self._quantity * self._unit_price

    def __str__(self):
        return f'{self.get_quantity()} {self.get_name()} @ ${self.get_unit_price()}/each - ${self.get_total_price()}'


class ShoppingCart:

    def __init__(self):
        self._items = []

    def add_item(self, item):
        self._items.append(item)

    def receipt(self):
        value = ""
        total = 0
        for item in self._items:
            value += f'{item}\n'
            total += item.get_total_price()
        value += f'Grand Total: ${total}'

        return value
from unittest import TestCase
from classes import Item, ShoppingCart

class TestItem(TestCase):
    def test_get_total_price(self):
        # arrange
        expected_name = 'bananas'
        expected_price = .3
        expected_quantity = 7
        expected_string = "7 bananas @ $0.3/each - $2.1"
        item = Item(expected_name, expected_price, expected_quantity)

        # act
        actual_string = str(item)

        # assert
        self.assertEqual(expected_string, actual_string)


class TestShoppingCart(TestCase):
    def test_receipt(self):
        # arrange
        cart = ShoppingCart()
        cart.add_item(Item("bananas", .3, 7))
        cart.add_item(Item("apples", .75, 5))
        expected_receipt = """7 bananas @ $0.3/each - $2.1
5 apples @ $0.75/each - $3.75
Grand Total: $5.85"""

        # act
        actual_receipt = cart.receipt()

        # assert
        self.assertEqual(expected_receipt, actual_receipt)
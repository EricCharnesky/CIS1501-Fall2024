from classes import Item, ShoppingCart

cart = ShoppingCart()

option = ""

while option != "done":
    if option == "add":
        name = input("Enter the item name")
        unit_price = float(input("enter the unit price"))
        quantity = float(input("enter the quanitty"))
        item = Item(name, unit_price, quantity)
        cart.add_item(item)

    elif option == "receipt":
        print(cart.receipt())

    option = input("Do you want to (add) an item, print the (receipt), or be (done)")
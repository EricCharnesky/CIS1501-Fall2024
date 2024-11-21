from classes import Item, ShoppingCart
import os


cart = ShoppingCart()

option = ""

while option != "done":
    if option == "add":
        name = input("Enter the item name")
        unit_price = float(input("enter the unit price"))
        quantity = float(input("enter the quantity"))
        item = Item(name, unit_price, quantity)
        cart.add_item(item)

    elif option == "receipt":
        print(cart.receipt())

    elif option == "save":
        name = input("Enter the name of the store for this cart")
        # output = open(f"{name}.txt", 'w')
        # output.write(str(cart.get_number_of_items()) + "\n")
        # output.write(cart.get_line_for_file())
        # output.close()

        # using with makes sure the file gets closed automatically when the block is done
        with open(f"{name}.txt", 'w') as output:
            output.write(str(cart.get_number_of_items()) + "\n")
            output.write(cart.get_line_for_file())

    elif option == 'load':
        cart = ShoppingCart()
        name = input("Enter the name of the store for this cart")
        if os.path.exists(f"{name}.txt"):
            cart_file = open(f"{name}.txt")
            number_of_items = int(cart_file.readline())
            for items in range(number_of_items):
                line = cart_file.readline()
            #for line in cart_file.readlines():
                item_data = line.split("|")
                item = Item(item_data[0], float(item_data[1]), int(float(item_data[2].strip())))
                cart.add_item(item)
            print(f"{name} cart was loaded")

    option = input("Do you want to (add) an item, print the (receipt), (save), (load), or be (done)")
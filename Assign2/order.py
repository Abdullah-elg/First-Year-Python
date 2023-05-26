from pizzaReceipt import generateReceipt

TOPPINGS = ("ONION", "TOMATO", "GREEN PEPPER", "MUSHROOM", "OLIVE", "SPINACH", "BROCCOLI", "PINEAPPLE",
            "HOT PEPPER", "PEPPERONI", "HAM", "BACON", "GROUND BEEF", "CHICKEN", "SAUSAGE")
sizes = ["S", "M", "L", "XL"]
pizza = []

quest = input("Do you want to order a pizza? ")

# loops so that if you keep answering yes to the question it orders multiple pizzas
while quest.upper() != 'NO' and quest.upper() != 'Q':
    newTop = []

    size = input("Choose a size: S, M, L, or XL: ")
    # loops till the answer to the question is part of the parameter
    while size.upper() not in sizes:
        size = input("Choose a size: S, M, L, or XL: ")

    top = input("Type in one of our toppings to add it to your pizza. To see the list of toppings, enter \"LIST\". When you are done adding toppings, enter \"X\"\n")
    # loops till the user is done adding toppings and enters 'x'
    while top.upper() != 'X':
        # if the user types 'list' it prints the list of toppings
        if top.upper() == 'LIST':
            print(TOPPINGS)
            top = input("Type in one of our toppings to add it to your pizza. To see the list of toppings, enter \"LIST\". When you are done adding toppings, enter \"X\"\n")
        # if the user types a topping it adds that topping to the pizza
        elif top.upper() in TOPPINGS:
            print("Added {} to your pizza".format(top.upper()))
            newTop.append(top.upper())
            top = input("Type in one of our toppings to add it to your pizza. To see the list of toppings, enter \"LIST\". When you are done adding toppings, enter \"X\"\n")
        # if the user types anything else it prints 'Invalid topping'
        else:
            print('Invalid Topping')
            top = input("Type in one of our toppings to add it to your pizza. To see the list of toppings, enter \"LIST\". When you are done adding toppings, enter \"X\"\n")
    # adding the pizza to a list so that multiple pizzas can be on the same receipt
    pizza.append((size.upper(), newTop))
    print(pizza)
    quest = input("Do you want to continue ordering? ")

print()
# calls the function for receipt with all the pizzas in the order
generateReceipt(pizza)

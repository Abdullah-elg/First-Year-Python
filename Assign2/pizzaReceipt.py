def generateReceipt(pizzaOrder):
    # if there is a value input for the pizza it runs the code
    if pizzaOrder:
        receipt = "Your order: \n"
        total = 0
        num = 1
        # finds the size of the pizza and adjusts the prices based on that
        for x in pizzaOrder:
            size = x[0].upper()
            toppings = x[1]
            if size == 'S':
                price = [7.99, 0.50]
            elif size == 'M':
                price = [9.99, 0.75]
            elif size == 'L':
                price = [11.99, 1.00]
            elif size == 'XL':
                price = [13.99, 1.25]
            # adding pizza and price to the receipt
            receipt += "Pizza {}: {}            {:>20.2f}\n".format(num, size, price[0])
            total += price[0]
            # adding toppings to the receipt
            for n in toppings:
                receipt += "- {}\n".format(n)
            # adding extra topping fee to the receipt
            if len(toppings) > 3:
                for e in range(len(toppings)-3):
                    receipt += "Extra Topping ({})          {:>15.2f}\n".format(size, price[1])
                    total += price[1]
            num += 1
        # adding tax to the receipt
        receipt += "Tax:            {:>26.2f}\n".format(total*0.13)
        total *= 1.13
        # adding total to the receipt
        receipt += "Total:          {:>26.2f}".format(total)
    # if there is no value input for the pizza it prints 'You did not order anything'
    else:
        receipt = "You did not order anything"
    print(receipt)

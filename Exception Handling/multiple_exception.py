def process_order(car, quantity):
    try:
        price = {"BMW" : 1000000}[car]

        cost = price * quantity

        print(f"The Total Cost : {cost}")

    except KeyError:
        print("Sorry cat not Available")

    except TypeError:
        print("Quantity must be in number")

# process_order("BMW", 2)

process_order("Audi", 3)

# process_order("BMW", "Three")
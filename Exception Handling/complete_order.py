class BmwModelNotFound(Exception):
    pass

def bmw_model(model, quantity):

    available = {"M8" : 50000000, "M4" : 17000000, "M3" : 30000000 }
    
    try:
        if model not in available:
            raise BmwModelNotFound(f"Your Model {model} is Unavailable")

        elif not isinstance(quantity, int):
            raise TypeError(f"Your Quantity {quantity} is Not an Integer")

        cost = available[model] * quantity

        print(f"\nSo, your total cost of Model {model} for {quantity} of cars : {cost}")

    except Exception as e:
        print("\nError : ", e)

    finally:
        print("\nvisit Again ..... :)")


bmw_model("M4", 4)

bmw_model("M6", 4)

bmw_model("M8", "four")
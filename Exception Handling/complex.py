orders = {"BMW": 4, "Audi": 2, "Mercedes": 1, "Toyota": 3, "unknown" : 0}

def Brand(car):
    try:
        orders[car]
        if "unknown" == car:
            raise ValueError("Enter A Vaild or Available Car Name.")
        print(f"We Have Stock of {car}.... :)")

    except Exception as e:
        print(f"[ERROR] : ", e)

    finally:
        print("Vist Again...")

w = input("Enter the car you want : ")
Brand(w)
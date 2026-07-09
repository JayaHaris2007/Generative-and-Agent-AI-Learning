car = ["BMW", "out of stock", "Audi", "Mercedes", "discontinued", "Toyota"]

for brand in car :
    if brand == "out of stock":
        continue

    elif brand == "discontinued":
        print("Discontinued Item found")
        break
    
    print(f"Cars brand : {brand}")


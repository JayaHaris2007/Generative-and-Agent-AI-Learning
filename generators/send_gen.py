def car_customer():
    print("welcome ! What car would you like to buy ?")

    order = yield

    while True:
        print(f"Your order is {order}")
        order = yield


showroom = car_customer()
next(showroom)  # Start the generator

showroom.send("Toyota")  # Send the first order
showroom.send("Honda")  # Send the second order 
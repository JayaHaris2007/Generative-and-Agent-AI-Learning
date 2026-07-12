def local_car():
    yield "BMW"
    yield "Audi"

def import_car():
    yield "Toyota"
    yield "Honda"

def total_car():
    yield from local_car()
    yield from import_car()

def get_car():
    for car in total_car():
        yield car
    
cars = list(get_car())


def car_showroom():
    print("car list:", cars)

    car = input("Enter the car you want to buy: ")

    if car in cars:
        order = yield "so your order is: " + car

    else:
        yield "Sorry, we don't have that car in our showroom."

showroom = car_showroom()
print(next(showroom))  # Start the generator and get the first message

showroom.close()  # Close the generator
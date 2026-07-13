class Car:
    def __init__(self):
        self.brand()

    def brand(brand):
        return brand

# print(type(Car))

class Bike:
    def __init__(self):
        self.brand()

    def brand(brand):
        return brand

Audi = Car.brand("audi")

print(Audi)

# print(type(Audi) is Car)

print(type(Audi) is Bike)
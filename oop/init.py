class Car:


    def __init__(self, type, brand) :
        self.type = type
        self.brand = brand

    def details(self):
        return f"Car Type {self.type} Brand of {self.brand}"


n = int(input("Enter The Numbers Cars You Want to Store : "))

cars = []

for i in range(n):
    type = input(f"Enter The Type {i} : ")
    brand = input(f"Enter The Brand {i} : ")

    car = Car(type=type, brand=brand)
    cars.append(car)

for car in cars:
    print(car.details())
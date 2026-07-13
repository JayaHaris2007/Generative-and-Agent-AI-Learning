class Car_Model:
    brand = "Toyota"

    def describe(self):
        return f"Avialable Car Brand : {self.brand}."
    
car = Car_Model()
print(car.describe())  # Output: This is a Toyota car.
print("Printed With Self Argument : " , Car_Model.describe(car))  # Output: This is a Toyota car.

car2 = Car_Model()
car2.brand = "BMW"
print(car2.describe())  # Output: This is a BMW car.
print("Printed With Self Argument : " , Car_Model.describe(car2))  # Output: This is a BMW car.
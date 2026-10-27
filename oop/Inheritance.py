class car:
    def __init__(self, model, brand):
        self.brand = brand
        self.model = model

class models(car): # Inheritance

    def model_number(self):
        print(f"Model : {self.model}\nBrand : {self.brand}")

# cars = models("M4 Comptetion", "BMW")

# cars.model_number()

class numbers: 
    cars = models

    def show(self):
        self.cars("X5", "BMW").model_number() #Composition


num = numbers()
num.show()
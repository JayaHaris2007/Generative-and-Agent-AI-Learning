class Car:

    @staticmethod # they are not bound to the class or instance, they are just functions defined inside a class

    def clean_car(text):
        return [item.strip() for item in text.split(",")]


raw = " BMW , Audi , Mercedes , Toyota "

# obj = Car()
# obj.clean_car(raw) #normal Mehtod

print(Car.clean_car(raw)) #Static Method
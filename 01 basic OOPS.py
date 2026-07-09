class car:
    def __init__(self, model, color, brand):
        self.model = model
        self.color = color
        self.brand = brand

    def display(self):
        print(f"Car Model: {self.model}")
        print(f"Car Color: {self.color}")
        print(f"Car Brand: {self.brand}")

bmw = car("M5", "Black", "BMW")
bmw.display()

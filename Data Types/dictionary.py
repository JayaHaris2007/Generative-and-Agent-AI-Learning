# car_model = dict(type="Sports", name="BMW", color="navy blue", value=10000000)
# print(f"Car Model: {car_model}")  # Output: Car Model

car_specs = {}
car_specs["Model"] = "M4 Competition"
car_specs["Engine"] = "3.0L Twin-Turbo Inline-6"

# print(f"car_specs: {car_specs['Model']}")
# print(f"car_specs all: {car_specs}")
# del car_specs["Engine"]
# print(f"car_specs after deletion: {car_specs}")

# print(f"the Model is availabe or not in the dictionary: {'Model' in car_specs}")

car = {
    "Type": "Sports",
    "Name": "BMW",
    "Color": "navy blue",
    "Value": 10000000
}

# print(f"Car dictionary keys Model: {car.keys()}\n")  # Output: Car Model

# print(f"Car dictionary values Model: {car.values()}\n")  # Output: Car Model

# print(f"Car dictionary items Model: {car.items()}\n")  # Output: Car Model

# last_car_key_value = car.popitem()
# print(f"\nLast car key value: {last_car_key_value}\n")  # Output

# car.update(car_specs)
# print(f"Updated car dictionary: {car}\n")  # Output: Updated car dictionary

# car_seater = car.get("Seater", "No Seater Mentioned")
# print(f"Car seater: {car_seater}\n")  # Output: Car seater

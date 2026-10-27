car_parts = ["engine", "wheels", "doors", "windows", "seats"]
print(f"Car Parts: {car_parts}")  # Output: Car Parts: ['engine', 'wheels', 'doors', 'windows', 'seats']

car_parts.append("mirrors")
print(f"Updated Car Parts: {car_parts}")  # Output: Updated Car Parts:

car_parts.remove("windows")
print(f"Car Parts after removing windows: {car_parts}")  # Output: Car Parts after removing windows: ['engine', 'wheels', 'doors', 'seats', 'mirrors']

india_car_brands = ["tata", "mahindra", "maruti", "honda", "hyundai"]

foriegn_car_brands = ["bmw", "audi", "mercedes", "toyota", "ford"]
print(f"Foreign Car Brands: {foriegn_car_brands}")  # Output: Foreign Car Brands: ['bmw', 'audi', 'mercedes', 'toyota', 'ford']

foriegn_car_brands.extend(india_car_brands)
print(f"All Car Brands: {foriegn_car_brands}")  # Output: All Car Brands: ['bmw', 'audi', 'mercedes', 'toyota', 'ford', 'tata', 'mahindra', 'maruti', 'honda', 'hyundai']

car = ["BMW", "LAMBORGINI", "FERRARI", "MERCEDES", "AUDI"]
print(f"Car Brands: {car}")  # Output: Car Brands: ['BMW', 'LAMBORGINI', 'FERRARI', 'MERCEDES', 'AUDI']
car.insert(2, "MACLAREN")
print(f"Updated Car Brands: {car}")  # Output: Updated Car Brands: ['BMW', 'LAMBORGINI', 'MACLAREN', 'FERRARI', 'MERCEDES', 'AUDI']

car = ["BMW", "LAMBORGINI", "FERRARI", "MERCEDES", "AUDI"]

print(f"Car Brands: {car}")  # Output: Car Brands: ['BMW', 'LAMBORGINI', 'FERRARI', 'MERCEDES', 'AUDI']

last_added_car = car.pop()
print(f"Last Added Car: {last_added_car}")  # Output: Last Added Car

car = ["BMW", "LAMBORGINI", "FERRARI", "MERCEDES", "AUDI"]
print(f"Car Brands: {car}")  # Output: Car Brands: ['BMW', 'LAMBORGINI', 'FERRARI', 'MERCEDES', 'AUDI']

car.reverse()
print(f"Reversed Car Brands: {car}")  # Output: Reversed Car Brands: ['AUDI', 'MERCEDES', 'FERRARI', 'LAMBORGINI', 'BMW']

car = ["BMW", "LAMBORGINI", "FERRARI", "MERCEDES", "AUDI"]
print(f"Car Brands: {car}")  # Output: Car Brands: ['BMW', 'LAMBORGINI', 'FERRARI', 'MERCEDES', 'AUDI']

car.sort()
print(f"Sorted Car Brands: {car}")  # Output: Sorted Car Brands: ['AUDI', 'BMW', 'FERRARI', 'LAMBORGINI', 'MERCEDES']

number = [5, 2, 9, 1, 7]
print(f"Numbers: {number}")  # Output: Numbers: [5, 2, 9, 1, 7]

print(f"Max Number: {max(number)}")

print(f"Min Number: {min(number)}")

mnc_india = ["Zoho", "HCL", "TCS", "Infosys", "Wipro"]

mnc_foreign = ["Google", "Microsoft"]

mnc_combined = mnc_india + mnc_foreign 

print(f"Combined MNCs: {mnc_combined}")  # Output: Combined MNCs: ['Zoho', 'HCL', 'TCS', 'Infosys', 'Wipro', 'Google', 'Microsoft']  

car = ["BMW", "AUDI"] * 3
print(f"Repeated Car Brands: {car}")  # Output: Repeated Car Brands:

car = bytearray(b"Maclaren")
print(f"Bytes : {car}")  # Output: Bytes : bytearray(b'Maclaren')
car = car.replace(b"Maclaren", b"Ferrari")
print(f"Updated Bytes : {car}")  # Output: Updated Bytes : bytearray(b

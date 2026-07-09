good_cars = [
    "bmw","mercedes","mclaren","lambo","bmw","ford"
]

cars = {car for car in good_cars}

print(cars)

car_specs = {
    "bmw": ["v8", "trubo", "racing kit"],
    "ford": ["v8", "nitro", "drift Kit"],
    "porche": ["inline-6", "turbo", "racing kit"],
}

unique_spec = {specs for details in car_specs.values() for specs in details}

print(unique_spec)
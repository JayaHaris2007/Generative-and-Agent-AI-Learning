def car():
    yield "Car 1 : bmw"
    yield "Car 2 : mclaren"
    yield "Car 3 : ford"

showroom = car()

print(next(showroom))
# print(next(showroom))
# print(next(showroom))
# print(next(showroom)) # gets error


# for brand in showroom:
#     print(brand)
class India_car:
    production = "India" # property 

# print(India_car.production)

India_car.engine = True

# print(India_car.engine)

car = India_car()

print("Car Production : ",car.production)
print("Car Engine : ",car.engine)

India_car.engine = False

print("Car Production : ",car.production)
print("Car Engine : ",car.engine)

car.max_speed = 200

print("car Max Speed : ",car.max_speed)

print("Overall Car details : ", 
      car.production, car.engine, car.max_speed)
orders = {"BMW": 4, "Audi": 2, "Mercedes": 1, "Toyota": 3}

try:
    orders["Lamborghni"]  # This will raise a TypeError since the dictionary is not callable

except KeyError:
    print("the Key your trying fetch it doesn't exists... :)")

print("This line pass after error occured")
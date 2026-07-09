value = 13
reminder = value % 5;

if reminder :
    print(f"not divisible, reminder value is {reminder}")

value = 13

if (remainder := value % 5) :
    print(f"not divisible, reminder value is {remainder}")

available = ['apple', 'banana', 'orange', 'grape', 'kiwi']

if (fruit := input("Enter your fruit name : ")) in available:
    print(f"getting your {fruit}")

else :
    print(f"the fruit {fruit} not available ")

car = ["bmw", "porsche", "mercedes", "jagaur"]

print ("available Cars : ", car)

while (brand := input("Choose Car brand : ").lower()) not in car :
    print(f"Sorry, brand {brand} is not available")


print(f"you choice {brand} car")
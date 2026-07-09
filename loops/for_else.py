student = [("Praveen", 23), ("Nihal", 20), ("Sanjay", 20), ("Jaya Haris", 20)]

for name, age in student:
    if age >= 18 :
        print(f"{name} is eligible as child")
        break
    
else :
    print("no one is a child")


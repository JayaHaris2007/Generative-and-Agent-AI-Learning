class Car: 
    engine = "v8"  # class attribute
    max_speed = 200  # class attribute
    # color = "Red"  # class attribute

bmw = Car()
print("Default Engine:", bmw.engine)  # Output: v8
# print(bmw.max_speed)  # Output: 200

bmw.engine = "v6"  # instance attribute shadows class attribute
print("Changed Engine:", bmw.engine)  # Output: v6

# mercedes = Car()
# print("Direct view inside class : ", mercedes.engine)  # Output: v8

bmw.color = "Black"  # adding a new instance attribute
print("BMW Color:", bmw.color)  # Output: Black

del bmw.engine  # delete instance attribute
print("After Deletion Engine:", bmw.engine)  # Output: v8 (falls back to class attribute)

# del bmw.color  # delete instance attribute
# print("After Deletion Color:", bmw.color)  # This will raise an Attribute

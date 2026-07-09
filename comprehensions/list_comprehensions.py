menu = [
    "masala chai",
    "green tea",
    "iced lemon tea",
    "Ginger chai"
]

iced_tea = [tea for tea in menu if "chai" in tea]

print(f"Available Tea : {iced_tea}")
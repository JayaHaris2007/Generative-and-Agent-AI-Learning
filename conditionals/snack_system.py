snack = input("Enter your prefeared snack: ").lower()

# print(f"User Said : {snack}")

if snack == "cookies" or snack == "samosa" :
    print('Good Choice!')
    print(f"Here is your sancks {snack}")

else:
    print(f"sorry, {snack} is not aviable ")
    print("we only serve cookies and samosa")
device_status = "active"
temperature = 38

if device_status == "active":
    print("\nDevice is online")
    if temperature > 35:
        print("|--High Temperature\n")

    else : 
        print("|--Device is normal\n")

else:
    print("\nDevice is offline\n")
order_amount = int(input("Enter The Order ammount : "))

delivery_charge = 0 if order_amount > 300 else 30

print(f"delivery fees is : {delivery_charge}")
order = ["haris", "nihal", "praveen", "sanjay", "elango"]

bill = [170, 300, 200, 150, 160]

for name, amount in zip(order, bill):
    print(f"order ready for : {name} and the bill amount is : {amount}")


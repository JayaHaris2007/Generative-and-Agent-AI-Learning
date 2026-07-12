def infinite_petrol():
    count = 1
    while True:
        yield f"Petrol Pump refill : {count}"
        count += 1

refill_station = infinite_petrol()
user2 = infinite_petrol()

for _ in range(5):
    print("User 1:", next(refill_station))

for _ in range(3):
    print("User 2:", next(user2))
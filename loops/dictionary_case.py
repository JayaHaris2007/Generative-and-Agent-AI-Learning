# users = [
#     {"id" : 1, "total" : 100, "coupon" : "P20"},
#     {"id" : 2, "total" : 250, "coupon" : "A31"},
#     {"id" : 3, "total" : 170, "coupon" : "G42"},
# ]

# discounts = {
#     "P20" : (0.2, 0),
#     "A31" : (0.5, 20),
#     "G42" : (0, 10),
# }

# for user in users :
#     percent, fixed = discounts.get(user["coupon"], (0, 0))

#     discount = user["total"] * percent + fixed

#     print(f"{user ['id']} paid {user['total']} and got discount for next visit of rupees for next visit of rupees {discount}")
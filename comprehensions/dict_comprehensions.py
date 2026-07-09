car_price_inr = {
    "bmw" : 1500,
    "mclarn" : 1500,
    "lambo" : 2000
}

car_price_usd = { car:price / 95 for car, price in car_price_inr.items() }

print("converted to USD : ", car_price_usd)
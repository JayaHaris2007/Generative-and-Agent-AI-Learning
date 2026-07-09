def add_vat(price, vat_rate):
    return price * (100 + vat_rate)/100

order = [150, 250, 100]

for price in order:
    final_amount = add_vat(price, 10)
    print(f"Your With Out VAT : {price} and total Bill including VAT : {final_amount}")


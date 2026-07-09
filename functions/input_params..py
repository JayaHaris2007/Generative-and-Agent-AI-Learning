# chai = "Ginger chai"

# def prepare_chai(order):
#     print(f"Preparing your {order}...")

# prepare_chai(chai)
# print(chai)

# chai = [1, 2, 3]

# def edit_chai(cup):
#     cup[1] = 42

# edit_chai(chai)
# print(chai)    

# def make_chai(tea, milk, sugar):
#     print(f"Making chai with {tea}, {milk}, and {sugar}.")

# make_chai("green tea", "almond milk", "honey") #postional

# make_chai(milk="oat milk", sugar="stevia", tea="black tea") #keyword

# def special_chai(*ingredients, **extras):
#     print("Ingredients:", ingredients)
#     print("Extras:", extras)

# special_chai("green tea", "almond milk", sugar="honey", spice="cinnamon")

# def chai_order(order=[]):
#     order.append("chai")
#     print("Current order:", order)

def chai_order(order=None):
    if order is None:
        order = []

    order.append("chai")
    print("Current order:", order)

chai_order()  # Current order: ['chai']
chai_order()  # Current order: ['chai', 'chai']
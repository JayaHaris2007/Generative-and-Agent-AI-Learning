import threading
import time

def take_order():
    for i in range(1, 4):
        print(f"Order Number : {i}")
        time.sleep(2)

def build_order():
    for i in range(1, 4):
        print(f"builded car order {i}")
        time.sleep(3)

get_order = threading.Thread(target=take_order)
prepare_order = threading.Thread(target=build_order)

get_order.start()
prepare_order.start()

get_order.join()
prepare_order.join()

print("Shop Completed And Closed ..... :) ")
from multiprocessing import Process

import time

def prepare_order(order):

    print(f"Starting preparing car number {order}")
    time.sleep(5)
    print(f"Completed preparing car number {order}")

if __name__ == "__main__":
    car_maker = [
        Process(target=prepare_order, args=(f"Car Maker #{i+1}", ))
        for i in range(3)
    ]

    for p in car_maker:
        p.start()

    for p in car_maker:
        p.join()

    print("Call Build Are Completed ..... :)")
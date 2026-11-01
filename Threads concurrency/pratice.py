import threading
import time

def  car_build(model, wait):
    print(f"Car {model} building...")

    time.sleep(wait)

    print(f"Car {model} completed.")

t1 = threading.Thread(target=car_build, args=("BMW M4", 3))
t2 = threading.Thread(target=car_build, args=("BMW M3", 2))
t3 = threading.Thread(target=car_build, args=("BMW M5", 4))

start = time.time()

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

end = time.time()

print(f"Total Time : {end - start:.2f} seconds")
import threading

import time 

def chat():
    count = 0

    print(f"{threading.current_thread().name} is started")

    for _ in range(100_000_000):
        count += 1

    print(f"{threading.current_thread().name} is completed")

thread1 = threading.Thread(target=chat)

thread2 = threading.Thread(target=chat)

start = time.time()
thread1.start()
thread2.start()

thread1.join()
thread2.join()

end = time.time()

print(f"total time taken: {end - start:.2f} seconds")
from multiprocessing import Process
import time

def chat():
    count = 0 
    print("Process is stared")

    for _ in range(100_000_000):
        count += 1

    print("Process Ended")

if __name__ == "__main__":
    p1 = Process(target=chat)
    p2 = Process(target=chat)

    start = time.time()

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    end = time.time()

    print(f"time taken {end - start :.2f} seconds")
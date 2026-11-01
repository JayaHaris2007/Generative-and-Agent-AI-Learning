import threading
import requests
import time 

def downloads(url):
    print(f"Starting download from {url}")
    resp = requests.get(url)
    print(f"Finished Downloading {url}, size: {len(resp.content)}")

urls = [
    "https://httpbin.org/image/jpeg",
    "https://httpbin.org/image/png",
    "https://httpbin.org/image/svg"
]

start = time.time()
thread = []

for url in urls:
    t = threading.Thread(target=downloads, args=(url, ))
    t.start()
    thread.append(t)

for t in thread:
    t.join()

end = time.time()

print(f"Total time Taken : {end - start}")
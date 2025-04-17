import socket
import threading
from tqdm import tqdm
import numpy as np

ports = list(range(0, 10000))
host = input("Website: ")
lock = threading.Lock()

open_ones = np.array([])

def search(start, end):
    for port in range(start, end):
        #try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.5)
                print(f"Working on port: {port}")
                res = s.connect_ex((host, port))
                '''
                if res == 1:
                    print(f"{port}: Closed!")
                '''
                with lock:
                    if res == 0:
                        #print(f"{port}: Open!")
                        np.append(open_ones, port)
            #except:
                #return "Problem!"

num_threads = 500
threads = []
chunk_size = len(threads) // num_threads

for i in tqdm(range(num_threads), desc="Starting threads"):
    start = i * chunk_size
    end = start + chunk_size if i != num_threads - 1 else len(ports)
    t = threading.Thread(name=f"thread_{i}", target=search, args=(start, end))
    threads.append(t)
    t.start()


for thread in threads:
    thread.join()

print("Open ports:")
print(open_ones)
import socket
import threading
from tqdm import tqdm

ports = list(range(0, 10000))
host = input("Website: ")
lock = threading.Lock()

def search():
    with lock:
        for port in ports:
            #try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.settimeout(0.5)
                    res = s.connect_ex((host, port))
                    if res == 0:
                        print(f"{port}: Open!")
                    elif res == 1:
                        print(f"{port}: Closed!")
            #except:
                #return "Problem!"

num_threads = 500
threads = []
for i in tqdm(range(num_threads)):
    t = threading.Thread(name=f"thread_{i}", target=search, args=())
    threads.append(t)

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

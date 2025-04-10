import socket
import threading

port = 12435
host = '0.0.0.0'

stopper = False

def data_check(s):
    checked = False
    while not stopper:
        try:
            data, addr = s.recvfrom(1024)
            if data:
                if not checked:
                    print(f"Message from {addr}")
                    checked = True
                print(data.decode(), "\n")
        except Exception as e:
            print("Problem")
            print(e)
            break

def message_sent(s):
    global stopper
    while not stopper:
        try:
            message = input()
            if message == "/exit":
                stopper = True
                print("Closed!")
            s.sendto(message.encode(), ('192.168.1.43', port))
        except Exception as e:
            print("Problem 2")
            print(e)
            break

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((host, port))

        thread1 = threading.Thread(target=data_check, args=(s,))
        thread2 = threading.Thread(target=message_sent, args=(s,))
        thread1.start()
        thread2.start()

        thread1.join()
        thread2.join()

if __name__ == "__main__":
    main()
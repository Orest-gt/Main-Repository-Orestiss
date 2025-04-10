import socket
import threading

port = 12435
host = '0.0.0.0'

def data_check(s):
    while True:
        try:
            data, addr = s.recvfrom(1024)
            if data:
                print(f"Received from->{addr}: {data.decode()}")
        except Exception:
            print("Problem")
            break


def message_sent(s):
    while True:
        try:
            message = input("Message: ")
            s.sendto(message.encode(), ('192.168.1.43', port))
        except Exception as e:
            print("Problem 2")
            print(e)
            break

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.connect((host, port))
        '''
        running = True
        while running:
            print("...")
            message = input("Message: ")
            s.sendall(message.encode())
            data, addr = s.recvfrom(1024)
            print(f"Message: : {data.decode()}")
        '''
        thread1 = threading.Thread(target=data_check, args=(s,))
        thread2 = threading.Thread(target=message_sent, args=(s,))
        thread1.start()
        thread2.start()

        thread1.join()
        thread2.join()

if __name__ == "__main__":
    main()
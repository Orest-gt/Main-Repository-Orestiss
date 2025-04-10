import socket

port = 81
host = 'localhost'

def lstn(s):
    try:
        s.listen(1)
        #s.accept()
        conn, addr = s.accept()
        with conn:
            print(f"Connection from {addr}")
            conn.sendall(b"Hi!")
    except OSError:
        s.settimeout(1)
        lstn(s)

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        with s.bind((host, port)):
            lstn(s)

if __name__ == "__main__":
    main()

'''
Kinda wrong, i'm bored to fix it, i made a new one
'''

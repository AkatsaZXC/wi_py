import socket
import os
import threading
from queue import Queue

print_lock = threading.Lock()
q = Queue()


def threader():
    while True:
        port = q.get()
        port_scanner(port)
        q.task_done()


def port_scanner(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server = input("Enter remote host to scan: ")
        server_ip = socket.gethostbyname(server)
    except socket.gaierror:
        print('Hostname could not be resolved. Exiting.')
        exit()
    try:
        result = s.connect_ex((server_ip, port))
        if result == 0:
            print('Port {}:  OPEN'.format(port))
        s.close()
    except socket.error:
        print('Couldn`t connect to the server')
        exit()
    except KeyboardInterrupt:
        print("Exiting...")
        exit()


def main():
    for x in range(100):
        thread = threading.Thread(target=threader)
        thread.daemon = True
        thread.start()

    for port in range(100):
        q.put(port)

    q.join()


if __name__ == '__main__':
    main()

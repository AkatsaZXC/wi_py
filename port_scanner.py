
import socket
import sys

def tcp_scanner(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server = input("Enter remote host to scan: ")
        server_ip = socket.gethostbyname(server)
    except socket.gaierror:
        print('Hostname could not be resolved. Exiting.')
        sys.exit()
    try:
        result = s.connect_ex((server_ip, port))
        if result == 0:
            print('Port {}:  OPEN'.format(port))
        s.close()
    except socket.error:
        print('Couldn`t connect to the server')
        sys.exit()
    except KeyboardInterrupt:
        print("Exiting...")
        sys.exit()



def main():
    for port in range(100):
        tcp_scanner(port)

if __name__ == '__main__':
    main()

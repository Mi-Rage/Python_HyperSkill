import argparse
import itertools
import socket

#
# ██████╗░░█████╗░░██████╗░██████╗░██╗░░░░░░░██╗░█████╗░██████╗░██████╗░      ██╗░░██╗░█████╗░░█████╗░██╗░░██╗███████╗██████╗░
# ██╔══██╗██╔══██╗██╔════╝██╔════╝░██║░░██╗░░██║██╔══██╗██╔══██╗██╔══██╗      ██║░░██║██╔══██╗██╔══██╗██║░██╔╝██╔════╝██╔══██╗
# ██████╔╝███████║╚█████╗░╚█████╗░░╚██╗████╗██╔╝██║░░██║██████╔╝██║░░██║      ███████║███████║██║░░╚═╝█████═╝░█████╗░░██████╔╝
# ██╔═══╝░██╔══██║░╚═══██╗░╚═══██╗░░████╔═████║░██║░░██║██╔══██╗██║░░██║      ██╔══██║██╔══██║██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗
# ██║░░░░░██║░░██║██████╔╝██████╔╝░░╚██╔╝░╚██╔╝░╚█████╔╝██║░░██║██████╔╝      ██║░░██║██║░░██║╚█████╔╝██║░╚██╗███████╗██║░░██║
# ╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚═════╝░░░░╚═╝░░░╚═╝░░░╚════╝░╚═╝░░╚═╝╚═════╝░      ╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝


def get_pass():
    numbers = [chr(i) for i in range(48, 58)]
    letters = [chr(i) for i in range(97, 123)]
    size = 1
    while True:
        my_iter = itertools.product(itertools.chain(numbers, letters), repeat=size)

        for i in my_iter:
            yield "".join(i)
        size += 1


parser = argparse.ArgumentParser()
parser.add_argument("host", help="Enter IP address")
parser.add_argument("port", help="Enter port from 1024 to 65535")

args = parser.parse_args()

ip_address = args.host
port = int(args.port)
address = (ip_address, port)
password = get_pass()
response = ""

with socket.socket() as client_socket:
    client_socket.connect(address)
    while response != "Connection success!":
        data = next(password).encode()
        client_socket.send(data)
        response = client_socket.recv(1024).decode()
    print(data.decode())

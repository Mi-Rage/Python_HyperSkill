import argparse
import socket


parser = argparse.ArgumentParser()
parser.add_argument("host", help="Enter IP address")
parser.add_argument("port", help="Enter port from 1024 to 65535")
parser.add_argument("message", help="Enter sending message")

args = parser.parse_args()

ip_address = args.host
port = int(args.port)
data = args.message.encode()
address = (ip_address, port)

with socket.socket() as client_socket:
    client_socket.connect(address)
    client_socket.send(data)
    response = client_socket.recv(1024)
    print(response.decode())

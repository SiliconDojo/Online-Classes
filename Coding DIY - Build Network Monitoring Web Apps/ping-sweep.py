import os

subnet = '192.168.1.'
command = 'ping -c 1 '
arg = '| grep time'

ip = 1
while ip <= 254:
    response = os.popen(f'{command} {subnet}{ip} {arg}').read()
    print(f'{subnet}{ip} -- {response}')
    ip += 1
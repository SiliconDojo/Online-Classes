import os
from time import sleep

command = 'ping -c 1 '
host_list = ['192.168.1.1','cnn.com','192.168.1.99','fox.com']
arg = '| grep time='

while True:
    os.system('clear')
    for host in host_list:
        try:
            response = os.popen(f'{command} {host} {arg}').read()
        except:
            response = ('problem')
        else:
            if response == '':
                response = 'no response\n'
        
        print(f'{host}\n{response}')
    
    sleep(10)
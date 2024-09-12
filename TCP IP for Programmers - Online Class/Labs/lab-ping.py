import os

command = 'ping -c 1 '
host_list = ['192.168.1.1','cnn.com','fox.com']


for host in host_list:
    try:
        response = os.popen(f'{command} {host}').read()
    except:
        response = ('problem')
    
    print(f'{host}\n{response}')
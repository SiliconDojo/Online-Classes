import os

command = 'ls -l'
# command = 'ping -c 1 cnn.com'
# command = 'ping -c 1 cnn.com | grep packet'

response = os.popen(command).read()
# response = os.popen(command).readlines()

print(response)
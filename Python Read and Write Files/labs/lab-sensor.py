from random import randint
from time import sleep

while True:
    temp = randint(0,100)
    color = ''
    if temp >= 80:
        color = 'red'
    elif temp < 80 and temp >= 50:
        color = 'green'
    else:
        color = 'blue'

    with open('sensor.html', 'w') as file:
        file.write('<meta http-equiv="refresh" content="5">')
        file.write(f'<p style="font-size:300;background-color:{color};">{temp}</p>')
    
    print(f'{temp}\t{color}')
    sleep(2)
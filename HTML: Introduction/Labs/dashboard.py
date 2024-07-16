from random import randint
from time import sleep

site = ['google.com','cnn.com','fox.com','tacobell.com']

while True:
    file = open('dashboard.html', 'w')
    file.write('<meta http-equiv="refresh" content="5">')
    file.write('<h1>Up/Down Dashboard</h1>')
    
    for host in site:
        condition = randint(0,2)

        if condition == 0:
            color = 'red'
        elif condition == 1:
            color = 'yellow'
        else:
            color = 'green'

        print(f'{host} {color}')
        file.write(f'<p style="background-color:{color};">{host}</p>\n')
    file.close()
    sleep(2)


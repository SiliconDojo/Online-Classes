import os
os.system('clear')

while True:
    command = input('Command: ')
    os.system('clear')

    try:
        response = os.popen(command).read()
    except:
        response = 'ERROR'
    finally:
        print(response)
        
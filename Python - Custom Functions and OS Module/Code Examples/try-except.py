try:
    with open('no-file.txt', 'r') as file:
        data = file.read()
except:
    print('ERROR')
# except Exception as error:
#     print(error)
else:
    print(data)
finally:
    print('Thanks for playing')
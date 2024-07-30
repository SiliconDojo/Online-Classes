while True:
    command = input('new or search: ')

    if command == 'new':
        name = input('Name: ')
        age = input('Age: ')
        with open('record.txt', 'a') as file_write:
            file_write.write(f'{name},{age}\n')

    if command == 'search':
        query = input('Query: ')
        with open('record.txt','r') as file_read:
            file_read = file_read.readlines()
        
        for record in file_read:
            if query in record:
                record = record.split(',')
                print(f'{record[0]}\t{record[1]}')
students = [{'name':'bob', 'age':19},
            {'name':'sue', 'age':21},
            {'name':'tim', 'age':10},
            {'name':'bill', 'age':33},
            {'name':'bobby', 'age':66},
            {'name':'bonnie', 'age':9},
            {'name':'phil', 'age':15}]

while True:
    min_age = int(input('Minimum Age: '))
    print('These Students Can Attend: ')
    for record in students:
        if record['age'] >= min_age:
                print(record['name'])


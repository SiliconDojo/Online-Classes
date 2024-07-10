nested = [{'name':'bob', 'age':17},
          {'name':'sue', 'age':12},
          {'name':'tim', 'age':33},
          {'name':'phil', 'age':24},
          {'name':'patty', 'age':5},
          {'name':'lorie', 'age':80},]

print(nested[2]['name'])

for record in nested:
    if record['age'] > 21:
        print(f'{record['name']} - {record['age']}')
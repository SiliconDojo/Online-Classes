with open('fake-data.csv') as file:
    file = file.readlines()

print(file[0])

for record in file[1:]:
    print(record)
    record = record.split(',')
    if int(record[2]) >= 50:
        print(f'{record[0]} {record[1]} {record[2]}')
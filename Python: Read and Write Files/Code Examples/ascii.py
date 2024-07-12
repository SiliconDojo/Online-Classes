name = [{'name':'bob','age':19},
        {'name':'sue','age':10},
        {'name':'phil','age':33},
        {'name':'sammy','age':50}]

with open('ascii.txt','w') as file:
    file.write('Students:\n')
    for student in name:
        file.write(f'\t{student["name"]}\t{student["age"]}\n')
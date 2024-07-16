money = {'owed':0.00, 'monthly_payment':0.00}
years = 0

money['owed'] = float(input('Starting Bill: '))
money['monthly_payment'] = float(input('Monthly Payment: '))

while money['owed'] >= 0:
    print(f'Year {years} = {money["owed"]}')
    money['owed'] = money['owed'] - (money['monthly_payment'] * 12)
    years += 1

print(f'Bill will take {years} years to pay off')
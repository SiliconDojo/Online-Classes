my_dict = {'name':'bob','age':19,'size':'large','disclaimer':True}

print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())

my_dict.update({'allergy':'peanut'})
print(my_dict)

my_dict.pop('size')
print(my_dict)
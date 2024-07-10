my_list = [3,4,7,1,33,5,55]

print(max(my_list))
print(min(my_list))
print(len(my_list))

total = 0
for x in my_list:
    total = total + x
average = total / len(my_list)

print(average)
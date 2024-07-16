my_list = ['bob', 'sue', 'bobby', 'bo', 'tim', 'tommy']

my_dict = {'name':'bob', 'age':19, 'gender':'male', 'size':'xl'}

for x in my_list:
    print(x)

for name in my_list:
    if 'bob' in name:
        print(name)

for key, value in my_dict.items():
    print(f'{key} - {value}')

for key, value in my_dict.items():
    print(f'{key.title()} - {str(value).upper()}')
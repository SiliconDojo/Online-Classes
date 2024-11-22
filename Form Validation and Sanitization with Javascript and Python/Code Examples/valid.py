import validators

def is_valid_input(input):
    if validators.url(input):
        print(f'{input} is a URL')
    elif validators.email(input):
        print(f'{input} is an Email')
    elif validators.domain(input):
        print(f'{input} is a Domain')
    elif validators.ipv4(input):
        print(f'{input} is an IP')
    else:
        print(f'{input} is not VALID')

while True:
    value = input("Input: ")
    is_valid_input(value)
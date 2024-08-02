def math(num1, num2):
    dict = {}
    dict['add'] = num1 + num2
    dict['sub'] = num1 = num2
    dict['mult'] = num1 * num2

    return dict

response = math(33, 400)

print(response)
print(type(response))

print(response['mult'])
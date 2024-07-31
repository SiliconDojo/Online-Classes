from requests import get

result = get('https://api.ipify.org')
print(result)
print(result.status_code)
print(result.headers)

# result_text = get('https://api.ipify.org').text
# print(result_text)

# result_json = get('https://api.ipify.org?format=json').json()
# print(result_json)

# print(result_json['ip'])
import html

def sanitize_html(input_string):
    return html.escape(input_string)

while True:
    value = input('User Input: ')
    print(sanitize_html(value))

from bottle import run, route, request, redirect, post

@route('/')
def index():
    form = '''
            New Note:
            <br>
            <form action="/process" method="post">
            Title: <input type="text" name="title">
            <br>
            Note: <input type="text" name="note">
            <input type="submit">
            </form>            
            '''
    try:
        with open('note-app.txt', 'r') as file:
            data = file.readlines()
            data_html = ''
            for record in data:
                value = record.split('||')
                data_html = f'''
                                <strong>{value[0]}</strong>
                                <p>{value[1]}</p>
                                <hr> 
                                {data_html}
                            '''
    except:
        data_html = ''

    page = f'{form} <br> {data_html}'

    return page

@post('/process')
def process():
    title = request.forms.get('title')
    note = request.forms.get('note')
    with open('note-app.txt', 'a') as file:
        file.write(f'{title}||{note}\n')
    redirect ('/')

run(host='localhost', port=8080)
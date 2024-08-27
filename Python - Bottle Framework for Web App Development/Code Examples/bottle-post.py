from bottle import run, route, post, request

@route('/')
def index():
    form =  '''
            <form action="/process" method="post">
                Name: <input type="text" name="name">
                <br>
                <input type="submit">
            </form>
            '''
    page = f'<h1>Web App</h1>{form}'
    return page

@post('/process')
def index_process():
    name = request.forms.get('name')

    message = f'Hello {name}'

    return message

run(host='localhost', port=8080)
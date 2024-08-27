from bottle import run, route

@route('/')
def index():
    page = '''
            <h1>Web Page</h1>
            <p>This is my very simple web page</p>
            '''

    return page

run(host='localhost', port=8080)
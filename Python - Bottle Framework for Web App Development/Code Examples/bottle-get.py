from bottle import run, route, get, request

@route('/')
@get('/')
def index():
    color = request.query.get('color')

    form =  '''
                <a href="/?color=red">Red</a>
                <br>
                <a href="/?color=green">Green</a>
                <br>
                <a href="/?color=yellow">Yellow</a>
                <br>
            '''
    page = f'''
                <h1>Web App</h1>
                <body style="background-color:{color};">
                {form}
                </body>
            '''
    return page

run(host='localhost', port=8080)
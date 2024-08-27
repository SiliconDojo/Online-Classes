from bottle import run, route, static_file

@route('/')
def index():
    file = 'image.png'
    page = f'''
                <link rel="stylesheet" type="text/css" href="/static/style.css">
                <body>
                    <h1>Static File</h1>
                    <img style="height:300px; width:auto;" src="/static/{file}">
                    <p>This is an embedded picture</p>
                </body>
            '''
    return page

@route('/static/<filename:path>')
def send_static(filename):
    print(filename)
    return static_file(filename, root='./static/')

run(host='localhost', port=8080)
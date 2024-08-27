from bottle import run, route, redirect

@route('/')
def index():
    site = 'http://cnn.com'
    redirect(site)

run(host='localhost', port=8080)
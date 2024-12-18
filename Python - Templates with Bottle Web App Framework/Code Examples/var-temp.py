from bottle import route, run, template

@route('/')
def index():
    name = '<a href="http://cnn.com">bob</a>'
    list = ['item1', 'item2', 'item3', 'item4']
    return template('template-var', name=name, list=list)

run(host='localhost', port='8080')
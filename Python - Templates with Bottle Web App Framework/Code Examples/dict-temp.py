from bottle import route, run, template

@route('/')
def index():

    people = {
            'sue': 19,
            'tim': 33,
            'frank':20
    }

    return template('template-dict', people=people)

run(host='localhost', port='8080')
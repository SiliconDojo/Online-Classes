from bottle import request, run, get

@get('/receive')
def receive_post():
    print(f'data -- {request}')
    print()
    print(request.query.get('userAgent'))
    print(request.query.get('city'))

run(host='localhost', port=8080)
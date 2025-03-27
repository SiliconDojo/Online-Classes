from bottle import run, route, static_file, post, request
import sqlite3
import os

pic_directory = './image_food'

def search(term):
    print(term)
    conn = sqlite3.connect('moondream-autocaption.db')
    cursor = conn.cursor()
    query = cursor.execute(f"SELECT * FROM image where description like ?", 
                           (f'%{term}%',)) 
    response = query.fetchall()
    print(query)
    conn.close()

    return response

@route('/image_food/<filename:path>')
def serve_static(filename):
    return static_file(filename, root='./image_food')

@post('/')
@route('/')
def index():
    query = request.forms.get('query')
    response = search(query)

    form = '''<form action="./" method="post">
            Search <input type="text" name="query">
            <input type="submit">
            </form>
            <hr>
            '''
    
    page=''
    
    for image, description in response:
        image = os.path.join(pic_directory, image)
        page += f'''<div 
                        style="height:400px;
                        width:200px;
                        display:inline-block;
                        border:2px solid black; 
                        display: flex; 
                        flex-direction: column; 
                        justify-content: flex-start; 
                        align-items: center; 
                        overflow: hidden;">
                <img src="{image}" 
                style="height:auto;
                width:200px;">
                <hr>
                {description}
                </div>
                '''
    
    page = f'''{form}
                <div style="display: flex; 
                flex-wrap: wrap; 
                align-items: flex-start;">
                {page}
                </div>'''
    
    return(page)

run(host='127.0.0.1', port='8080')
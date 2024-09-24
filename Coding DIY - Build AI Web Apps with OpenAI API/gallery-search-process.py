import requests
import sqlite3
import os 
import base64

pic_directory = 'search_pics'
os.makedirs(pic_directory, exist_ok=True)

database = 'gallery-search.db'

api_key = ' '

header = f'''
            <h1>Open AI App</h1>
            <p><a href="/">Home</a> <a href="/search">Search</a></p>
        '''

def db_create():
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS gallery(filename,description)')
    conn.commit()
    conn.close()

def db_insert(filename, description):
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO gallery(filename, description) VALUES(?,?)',(filename,description))
    conn.commit()
    conn.close()
    print(f'ADDED: {filename}\n{description}')

def db_search(filename):
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    query = cursor.execute('SELECT * FROM gallery where filename = ?',(filename,)) 
    query = query.fetchall()
    conn.close()
    print(f'SEARCH: {filename}\n{query}')
    return query

def ai(filename):
    filename = os.path.join(pic_directory, filename)
 
    with open(filename, "rb") as image_file:
        base64_image =  base64.b64encode(image_file.read()).decode('utf-8')

    headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
    }

    payload = {
    "model": "gpt-4o-mini",
    "messages": [
        {
        "role": "user",
        "content": [
            {
            "type": "text",
            "text": "What’s in this image? Be as specific as possible. Answer in up to 100 words.s"
            },
            {
            "type": "image_url",
            "image_url": {
                "url": f"data:image/jpeg;base64,{base64_image}"
            }
            }
        ]
        }
    ],
    "max_tokens": 300
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
    response = response.json()
    response = (response['choices'][0]['message']['content'])

    return response

db_create()

contents = os.listdir(pic_directory)

for pic in contents:
    if db_search(pic) == []:
        try:
            description = ai(pic)
            db_insert(pic, description)
        except:
            pass
    else:
        pass
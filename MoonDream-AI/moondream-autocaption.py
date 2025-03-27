import moondream as md
from PIL import Image
import os
import sqlite3

pic_directory = './image_food'

model = md.vl(model='./moondream-2b-int8.mf.gz')

image_list = os.listdir(pic_directory)
print(image_list)

query = 'what is in this picture. use as many proper nouns as possible. be very descriptive. state any brands in the picture'

def insert(picture, answer):
    conn = sqlite3.connect('moondream-autocaption.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS image(image text,description text)')
    cursor.execute('INSERT INTO image(image,description) VALUES(?,?)',(picture, answer))
    conn.commit()
    conn.close()

for pic in image_list:
    picture = os.path.join(pic_directory, pic)
    image = Image.open(picture)
    encoded_image = model.encode_image(image)

    answer = model.query(encoded_image, query)['answer']
    print(pic)
    print('\nDescription:', answer)
    insert(pic, answer)

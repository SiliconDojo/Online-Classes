from openai import OpenAI
from requests import get
import os

bias = 'add a bunny'

def ai(query):
    client = OpenAI()
    response = client.images.generate(
    model="dall-e-3",
    prompt=query,
    n=1,
    size="1024x1024" 
    )

    return response

while True:
    query = input('Image to Create: ')
    query = f'{query} {bias}'
    os.system('clear')
    response = ai(query)
    pic_name = f'{response.created}.png'

    response_image = get(response.data[0].url)
    with open(pic_name, 'wb') as file:
        file.write(response_image.content)

    with open('gallery.html', 'a') as gallery:
        gallery.write(f'<img style="height:200px; width:auto;" src="{pic_name}">')
    
    print(query)
    print(response_image)
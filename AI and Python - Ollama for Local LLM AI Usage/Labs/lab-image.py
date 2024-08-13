import ollama

def ai(image, query):
    response = ollama.chat(
    model='llava',
    messages=[
        {
        'role': 'user',
        'content': query,
        'images': [image],
        },
    ],
    )
    answer = response['message']['content']

    return answer

image = 'image.png'

action = ['Create a Title for this image',
          'Create a description of this image under 50 words',
          'provide 10 tags for this image in CSV format']

data = []
for query in action:
    response = ai(image, query)
    data.append(response)
    print(response)

with open('gallery.htm', 'w') as file:
    file.write(f'<img style="height:300px;width:auto;" src={image}>')
    file.write(f'<h1>{data[0]}</h1>')
    file.write(f'<p>{data[1]}</p>')
    file.write(f'<p><i>{data[2]}</i></p>')

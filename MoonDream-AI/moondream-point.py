import moondream as md
from PIL import Image

model = md.vl(model='./moondream-2b-int4.mf.gz')

picture = './img2.jpeg'
image = Image.open(picture)
encoded_image = model.encode_image(image)

query = 'people'
point_result = model.point(encoded_image, query)
print("Points:", point_result["points"])

with open('moondream-point.html', 'w') as file:
    file.write('''
               <div style="position: relative; 
               height: 400px; 
               width: auto; 
               display: inline-block;">
               ''')
    file.write(f'''
               <img src="{picture}" 
               style="height: 100%; 
               display: block;">
               ''')
    for point in point_result["points"]:
        x = point['x'] * 100
        y = point['y'] * 100
        print(f"{x} -- {y}")
        file.write(f'''
                   <div style="color:red; 
                   position: absolute; 
                   top:{y}%; 
                   left:{x}%;"
                   >X</div>
                   ''')
    file.write('</div>')
import moondream as md
from PIL import Image

# model = md.vl(model='./moondream-2b-int4.mf.gz')  # Initialize model
model = md.vl(model='./moondream-0_5b-int8.mf.gz')  # Initialize model

picture = './img2.jpeg'
image = Image.open(picture)
encoded_image = model.encode_image(image)

query = "face"
detect_result = model.detect(encoded_image, query) 
print("\nDetected:", detect_result["objects"])

with open('moondream-object.html', 'w') as file:
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
    for object in detect_result['objects']:
        x = object['x_min'] * 100
        y = object['y_min'] * 100
        width = (object['x_max'] - object['x_min']) * 100
        height = (object['y_max'] - object['y_min']) * 100
   
        print(f"{x} -- {width} / {y} -- {height}")
        file.write(f'''
                   <div style="color:red; 
                   position: absolute; 
                   border: 2px solid red;
                   top:{y}%; 
                   left:{x}%;
                   width:{width}%;
                   height:{height}%;"
                   ></div>
                   ''')
    file.write('</div>')
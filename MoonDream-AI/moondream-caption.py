import moondream as md
from PIL import Image

model = md.vl(model='./moondream-2b-int4.mf.gz')
# model = md.vl(model='./moondream-0_5b-int8.mf.gz')

picture = './img2.jpeg'
image = Image.open(picture)
encoded_image = model.encode_image(image)

# Caption any image (length options: "short" or "normal" (default))
caption = model.caption(encoded_image, "short")
print("Caption:", caption['caption'])

with open('moondream-caption.html', 'w') as file:
    file.write(f'''
               <div style="position: relative; 
               height: 400px; 
               width: auto; 
               display: inline-block;">

               <img src="{picture}" 
               style="height: 100%; 
               display: block;">
  
                <div>{caption['caption']}</div>
                
                </div>''')

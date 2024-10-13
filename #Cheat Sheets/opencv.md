# Open CV

## Create HTML Page with Bounding Boxes

This example scans an image for faces, it then creates and HTML page with an embedded image with bounding boxes around the faces.

You need to install Pillow so that you can get the dimensions of the picture.

<img width="220" alt="Screenshot 2024-10-13 at 10 56 35 AM" src="https://github.com/user-attachments/assets/4436a4d0-4ce1-4d5a-b8f7-cc248698af86">

```
#python3 -m pip install pillow

import cv2 as cv
from PIL import Image

picture = "unicorn.jpeg"

img = cv.imread(picture)
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
filter = cv.CascadeClassifier('./data/haarcascades/haarcascade_frontalface_alt.xml')
result = filter.detectMultiScale(img_gray, minNeighbors=5, minSize =(20,20))
img_pil = Image.open(picture)
img_width = img_pil.width
img_height = img_pil.height

f = open('./bounding-box.html', 'w')
f.write(f'''
        <div style="position:relative; border:5px solid black; height:{img_height}px; width:{img_width}px;">
        <img src="./{picture}">
        ''')

for (x, y, w, h) in result:
    print(f'Picture: {picture} x: {x} y: {y} Width: {w} Height: {h}')
    f.write(f'<div style="position:absolute; border:3px solid red; height:{h}px; width:{w}px; top:{y}px; left:{x}px;"></div>')
f.write(f'</div>')
f.close()

```

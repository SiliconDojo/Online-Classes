import cv2 as cv
from PIL import Image
import os

list_picture = os.listdir('./pics')
print(list_picture)

f = open("./gallery.html", "w")

for picture in list_picture:
    try:
        img = cv.imread(f'./pics/{picture}')
        img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        filter = cv.CascadeClassifier('./data/haarcascades/haarcascade_frontalface_alt.xml')
        #filter = cv.CascadeClassifier('./data/haarcascades/haarcascade_frontalface_default.xml')
        #filter = cv.CascadeClassifier('./data/haarcascades/haarcascade_fullbody.xml')
        #filter = cv.CascadeClassifier('./data/haarcascades/haarcascade_upperbody.xml')
        result = filter.detectMultiScale(img_gray, minNeighbors=5, minSize =(20,20))
        img_pil = Image.open(f'./pics/{picture}')
        img_width = img_pil.width
        img_height = img_pil.height
        f.write(f'''
                <div style="position:relative; border:5px solid black; height:{img_height}px; width:{img_width}px;">
                <img src="./pics/{picture}">
                ''')
        for (x, y, w, h) in result:
            print(f'Picture: {picture} x: {x} y: {y} Width: {w} Height: {h}')
            f.write(f'<div style="position:absolute; border:5px solid red; height:{h}px; width:{w}px; top:{y}px; left:{x}px;"></div>')
        f.write(f'</div><br>')
    except:
        pass
    
f.close()
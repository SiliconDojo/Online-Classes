import cv2 as cv
import os

list_picture = os.listdir('./pics')
print(list_picture)

filter = cv.CascadeClassifier('data/haarcascades/haarcascade_frontalface_alt.xml')

file = open('gallery.html', 'w')

for picture in list_picture:
    color = ''
    try:
        img = cv.imread(f'./pics/{picture}')
        img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        result = filter.detectMultiScale(img_gray, minNeighbors=5, minSize =(20,20))
        if len(result) > 0:
            color = 'green'
        else:
            color = 'red'
            
        file.write(f'<img style="height:200px; width:auto; border: 20px {color} solid;" src="./pics/{picture}">')
    except:
        pass
file.close()

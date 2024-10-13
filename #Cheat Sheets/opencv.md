# Open CV

## Standard Web Cam Detection

This is the standard script for object detection with the computers webcam.

**NOTE:** Camera Number is 0 by default, but on ARM Mac Systems you may need to change to 1

<img width="300" alt="Screenshot 2024-10-13 at 11 09 24 AM" src="https://github.com/user-attachments/assets/12a24533-136f-4958-997a-d9563c8bd94b">


```
#This is the standard webcam example from OpenCV
#From: https://docs.opencv.org/4.x/db/d28/tutorial_cascade_classifier.html
from __future__ import print_function
import cv2 as cv
import argparse
 
def detectAndDisplay(frame):
    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    frame_gray = cv.equalizeHist(frame_gray)
 
    #-- Detect faces
    faces = face_cascade.detectMultiScale(frame_gray)
    for (x,y,w,h) in faces:
        center = (x + w//2, y + h//2)
        frame = cv.ellipse(frame, center, (w//2, h//2), 0, 0, 360, (255, 0, 255), 4)
 
        faceROI = frame_gray[y:y+h,x:x+w]
        #-- In each face, detect eyes
        eyes = eyes_cascade.detectMultiScale(faceROI)
        for (x2,y2,w2,h2) in eyes:
            eye_center = (x + x2 + w2//2, y + y2 + h2//2)
            radius = int(round((w2 + h2)*0.25))
            frame = cv.circle(frame, eye_center, radius, (255, 0, 0 ), 4)
 
    cv.imshow('Capture - Face detection', frame)
 
parser = argparse.ArgumentParser(description='Code for Cascade Classifier tutorial.')
parser.add_argument('--face_cascade', help='Path to face cascade.', default='data/haarcascades/haarcascade_frontalface_alt.xml')
parser.add_argument('--eyes_cascade', help='Path to eyes cascade.', default='data/haarcascades/haarcascade_eye_tree_eyeglasses.xml')
#SDNOTE -- default= should be wither 0 or 1. 0 is default. 1 needed for ARM Macs
parser.add_argument('--camera', help='Camera divide number.', type=int, default=0)
args = parser.parse_args()
 
face_cascade_name = args.face_cascade
eyes_cascade_name = args.eyes_cascade
 
face_cascade = cv.CascadeClassifier()
eyes_cascade = cv.CascadeClassifier()
 
#-- 1. Load the cascades
if not face_cascade.load(cv.samples.findFile(face_cascade_name)):
    print('--(!)Error loading face cascade')
    exit(0)
if not eyes_cascade.load(cv.samples.findFile(eyes_cascade_name)):
    print('--(!)Error loading eyes cascade')
    exit(0)
 
camera_device = args.camera
#-- 2. Read the video stream
cap = cv.VideoCapture(camera_device)
if not cap.isOpened:
    print('--(!)Error opening video capture')
    exit(0)
 
while True:
    ret, frame = cap.read()
    if frame is None:
        print('--(!) No captured frame -- Break!')
        break
 
    detectAndDisplay(frame)
 
    if cv.waitKey(10) == 27:
        break
```

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

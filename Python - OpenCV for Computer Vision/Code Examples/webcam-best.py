#This script finds and only displays the largest "face" that it sees
#We use a lambda function to find that face with the greates Height and Width
#Based on: https://docs.opencv.org/4.x/db/d28/tutorial_cascade_classifier.html
from __future__ import print_function
import cv2 as cv
import argparse
 
def detectAndDisplay(frame):
    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    frame_gray = cv.equalizeHist(frame_gray)
 
    #-- Detect faces
    faces = face_cascade.detectMultiScale(frame_gray)

    if len(faces) > 0: #SD
        largest_face = max(faces, key=lambda face: face[2] + face[3]) #SD
        x, y, w, h = largest_face #SD
        
        center = (x + w//2, y + h//2)
        cv.putText(frame, f'X: {center[0]} Y: {center[1]}', (50, 50), cv.FONT_HERSHEY_SIMPLEX,1, (0, 255, 255), 2) #SD
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
parser.add_argument('--camera', help='Camera divide number.', type=int, default=1)
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
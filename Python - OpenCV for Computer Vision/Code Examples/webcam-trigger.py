#This script prints directions on the screen based on the location of the object
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
        cv.putText(frame, '+', (center), cv.FONT_HERSHEY_SIMPLEX,1, (0, 255, 255), 10) #SD
        command_y = ''
        command_x = ''
        if center[0] > 1220:
            command_x = 'left'
        elif center[0] < 700:
            command_x = 'right'
        else:
            command_x = ''

        if center[1] > 680:
            command_y = 'up'
        elif center[1] < 400:
            command_y = 'down'
        else:
            command_y = ''

        cv.putText(frame, f'X: {center[0]} Y: {center[1]}', (50, 120), cv.FONT_HERSHEY_SIMPLEX,5, (0, 255, 255), 5) #SD
        cv.putText(frame, command_y, (50,270), cv.FONT_HERSHEY_SIMPLEX,5, (0, 255, 255), 5) #SD
        cv.putText(frame, command_x, (50,420), cv.FONT_HERSHEY_SIMPLEX,5, (0, 255, 255), 5) #SD
 
    cv.imshow('Capture - Face detection', frame)
 
parser = argparse.ArgumentParser(description='Code for Cascade Classifier tutorial.')

parser.add_argument('--face_cascade', help='Path to face cascade.', default='data/haarcascades/haarcascade_frontalface_alt.xml')
#SDNOTE -- default= should be wither 0 or 1. 0 is default. 1 needed for ARM Macs
parser.add_argument('--camera', help='Camera divide number.', type=int, default=1)
args = parser.parse_args()
 
face_cascade_name = args.face_cascade
 
face_cascade = cv.CascadeClassifier()
 
#-- 1. Load the cascades
if not face_cascade.load(cv.samples.findFile(face_cascade_name)):
    print('--(!)Error loading face cascade')
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
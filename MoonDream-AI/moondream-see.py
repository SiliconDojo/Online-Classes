import moondream as md
from PIL import Image
import cv2
import time

def camera():
    # Open webcam (0 = default camera) - SD: M Processor Macs Use 1
    cap = cv2.VideoCapture(0)
    time.sleep(1)

    if not cap.isOpened():
        print("Cannot open webcam")
        exit()

    ret, frame = cap.read()

    if ret:
        cv2.imwrite("captured_image.jpg", frame)
        print("Image saved as captured_image.jpg")
    else:
        print("Failed to grab frame")

    cap.release()
    cv2.destroyAllWindows()


model = md.vl(model='./moondream-2b-int8.mf.gz')

while True:
    color = ''
    answer = ''
    camera()
    picture = './captured_image.jpg'
    image = Image.open(picture)
    encoded_image = model.encode_image(image)

    query = '''if person is wearing orange clothing say "good",
                else say "bad"'''
    
    answer = model.query(encoded_image, query)["answer"]

    query2 = '''if there is no one in say "empty"'''

    if answer.strip() == 'bad':
        answer = model.query(encoded_image, query2)["answer"]
        if answer.strip() == 'empty':
            answer = 'Room is Empty'
            color = 'grey'
        else:
            answer = 'Bad Person in Room'
            color = 'red'
    else:
        answer = 'Good Person is Room'
        color = 'green'

    print(f'Result: {answer}')

    with open('vision-alert.html', 'w') as file:
        file.write('<meta http-equiv="refresh" content="2">')
        file.write(f'<body style="background-color:{color};">')
        file.write(f'<img src="./captured_image.jpg" style="height:300px;width:auto;">')

import cv2
import numpy as np

my_webcam = cv2.VideoCapture(0)
color = ''

while True:
    validation, frame = my_webcam.read()
    if validation is not True:
        break
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    blur_frame = cv2.GaussianBlur(frame_gray, (45, 45),0)

    width = int(my_webcam.get(3))
    height = int(my_webcam.get(4))
    half_width = int(width/2)
    half_height = int(height/2)

    blur_frame[half_height-70:half_height+70, half_width-100:half_width+100] = frame_gray[half_height-70:half_height+70, half_width-100:half_width+100]

    rect = frame_gray[half_height-70:half_height+70, half_width-100:half_width+100]
    blur_frame[half_height-70:half_height+70, half_width-100:half_width-95] = 0
    blur_frame[half_height-70:half_height+70, half_width+95:half_width+100] = 0
    blur_frame[half_height-70:half_height-65, half_width-100:half_width+100] = 0
    blur_frame[half_height+65:half_height+70, half_width-100:half_width+100] = 0

    cv2.normalize(rect, rect, 0, 255, cv2.NORM_MINMAX)
    if 0 <= np.average(rect) < 50:
        color = 'Black'
    elif 50 <= np.average(rect) < 120:
        color = 'Gray'
    elif 120 <= np.average(rect):
        color = 'White'

    cv2.putText(blur_frame, color, (30,50), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 0), 2)

    cv2.imshow('output', blur_frame)
    if cv2.waitKey(1) == ord('q'):
        break
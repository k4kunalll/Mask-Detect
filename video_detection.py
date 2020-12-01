from detection_func import *
import cv2

video = cv2.VideoCapture(r'Enter Your Video Location here')

while (True):
    ret, img = video.read()
    img = show_inference(detection_model, img)
    cv2.imshow('LIVE', img)
    k = cv2.waitKey(1)

    if (k == 27):
        break
cv2.destroyAllWindows()
from detection_func import *
import os
import cv2
from datetime import datetime


def mask_detect(image, classes, score, boxes):
    for i in range(100):

        if (classes[i] == 2 and score[i] > 0.5):

            now = datetime.now()
            dt_string = now.strftime("%d_%m_%Y_%H_%M_%S")

            h, w = image.shape[0:2]
            # image.shape=[height,width,3]

            # coordinates of bounding boxes

            ymin, xmin, ymax, xmax = boxes[i]

            x1 = int(xmin * w)
            x2 = int(xmax * w)
            y1 = int(ymin * h)
            y2 = int(ymax * h)

            x = x2 - x1
            y = y2 - y1

            start_point = int(xmin * w), int(ymin * h)
            end_point = int(xmax * w), int(ymax * h)
            color = (0, 0, 0)
            thickness = 2
            radius = int(min(x, y) / 2)

            for i in range(10):
                rect = cv2.rectangle(image, start_point, end_point, color, thickness)

                file_name = os.path.join("WithoutMask_Images", dt_string + ".jpg")
                cv2.imwrite(file_name, rect)

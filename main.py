from detection_func import *
from mask_detect import *

import cv2

for i in TEST_IMAGE_PATHS:
    img = cv2.imread(str(i))
    img = cv2.resize(img, (1000, 640))

    img = show_inference(detection_model, img)
    cv2.imshow('IMG', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
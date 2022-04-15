import numpy as np
import cv2
from mss import mss
from PIL import Image

bouding_box = {'top': 38, 'left': 9, 'width': 1920, 'height': 1080}

sct = mss()

while True:
    sct_img = sct.grab(bouding_box)
    cv2.imshow('screen', np.array(sct_img))

    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        cv2.destroyAllWindows()
        break

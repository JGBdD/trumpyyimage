import cv2
from  PIL import Image , ImageFilter
import numpy as np


video = cv2.VideoCapture(0)
video.set(3,1280)
video.set(4,720)

offset = 0

if video.isOpened():
    while True:
        ret_v, frame = video.read()
        print(frame.shape)

        # frame[: , : , 0]  = +frame  [: , : ,0] + offset + frame[: , ::-1 , 0]
        # frame[: , : , 1] = -frame  [: , : ,1] + offset*2
        # frame[: , : , 2] = -frame  [: , : ,2] + frame[::-1 , : , 2]
        # offset += 1

        img =  Image.fromarray(frame).filter(ImageFilter.FIND_EDGES)
        frame = np.array(img)


        cv2.imshow("window" , frame)
        if cv2.waitKey(1) == ord("q"):
            break



    video.release()
    cv2.destroyAllWindwos()
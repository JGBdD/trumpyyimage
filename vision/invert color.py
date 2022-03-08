import cv2

video = cv2.VideoCapture(0)
video.set(3,1280)
video.set(4,720)

offset = 0

if video.isOpened():
    while True:
        ret_v, frame = video.read()
        print(frame.shape)

        frame[: , : , 0]  = -frame  [: , : ,0]
        frame[: , : , 1] = -frame  [: , : ,1]
        frame[: , : , 2] = -frame  [: , : ,2]
        offset += 1

        cv2.imshow("window" , frame)
        if cv2.waitKey(1) == ord("q"):
            break



    video.release()
    cv2.destroyAllWindwos()
import cv2 as cv
import HandTrackingModule as htm

wCam , hCam = 640,480

vid = cv.VideoCapture(0)
vid.set(3,wCam)
vid.set(4,hCam)

detector = htm.handDetector(min_detection_confidence=0.8)

# idNums = [8,12,16,20]
while True:
    success , img = vid.read()
    img = detector.findHands(img)
    cv.imshow('',img)
    # lmList = detector.findPos(img)
    # # print(lmList)
    # if len(lmList)!=0:
    #     fingers = []
    #
    #     # Thumb
    #     if lmList[4][1] > lmList[4 - 1][1]:
    #         fingers.append(1)
    #     else:
    #         fingers.append(0)
    #
    #     # 4 Fingers
    #     for id in idNums:
    #         if lmList[id][2] < lmList[id-2][2]:
    #             fingers.append(1)
    #         else:
    #             fingers.append(0)
    #     print(fingers)
    print(detector.fingersUp(img))

    if cv.waitKey(1) & 0xFF == ord('q'):
        break
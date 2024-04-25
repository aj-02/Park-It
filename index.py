import cv2
import numpy as np
import pickle
import cvzone
from twilio.rest import Client
from config import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN

account_sid = TWILIO_ACCOUNT_SID
auth_token = TWILIO_AUTH_TOKEN
client = Client(account_sid, auth_token)

cap = cv2.VideoCapture('carPark.mp4')



with open('carParkPos', 'rb') as f:
    posList = pickle.load(f)

width = 107
height = 48

def checkParkingSpace(image):

    spaceCounter = 0

    for pos in posList:
        x,y = pos
        imgCrop = image[y:y+height, x:x+width]
        message = client.messages.create(
            from_='+19283230285',
            body='There are free slots: {}'.format(spaceCounter),
            to='+919971324400'
        )
        count = cv2.countNonZero(imgCrop)
        cvzone.putTextRect(img,str(count),(x,y+height-3), scale = 1, thickness = 2, offset = 0)
        if count < 900:
            color = (0,255,0)
            thickness = 5
            spaceCounter = spaceCounter + 1
            print(message.sid)
        else:
            color = (0,0,255)
            thickness = 2

        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), color, thickness)

    cvzone.putTextRect(img, f'Free:  {spaceCounter} / {len(posList)}', (100,50), scale=3, thickness=5, offset=20)


while True:
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

    success, img = cap.read()

    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray,(3,3),1)
    imgThreshold = cv2.adaptiveThreshold(imgBlur,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV,25,16)
    imgMedian = cv2.medianBlur(imgThreshold,5)
    kernel = np.ones((3,3),np.uint8)
    imgDilate = cv2.dilate(imgMedian,kernel, iterations=1)

    checkParkingSpace(imgDilate)


    cv2.imshow('image123', img)
    cv2.waitKey(10)





    

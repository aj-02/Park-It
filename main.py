import cv2
import pickle

img = cv2.imread('carParkImg.png');
width = 107
height = 48
try:
    with open('carParkPos', 'rb') as f:
        posList = pickle.load(f)
except:
    posList = []

def mouseClick(events, x, y, flags, param):
    if events == cv2.EVENT_LBUTTONDOWN:
        posList.append((x,y))
    if events == cv2.EVENT_RBUTTONDOWN:
        for i, pos in enumerate(posList):
            x1,y1 = pos
            if x1<x<x1+width and y1<y<y1+height:
                posList.pop(i)

    with open('carParkPos', 'wb') as f:
         pickle.dump(posList,f)


while True:
    cv2.imshow('image', img)
    for pos in posList:
        cv2.rectangle(img, pos, (pos[0]+width,pos[1]+height), (255,0,255), 2)
    cv2.setMouseCallback('image',mouseClick)
    cv2.waitKey(1)
#!/usr/bin/env python
# coding: utf-8


import cv2
import mediapipe as mp
import time


cap=cv2.VideoCapture(0)
mpHands=mp.solutions.hands
hands=mpHands.Hands()
mpDraw=mp.solutions.drawing_utils


pTime=0
cTime=0

while True:
    success, img= cap.read()
    print(img)
    imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results=hands.process(imgRGB)
    
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id,lm in enumerate(handLms.landmark):
                #print(id,lm)
                h,w,c = img.shape     # height,weight and channells for image
                cx, cy = int(lm.x*w),int(lm.y*h)  # they are decimal places and converted into intergers (position of centered)
                #print(id,cx,cy)
                if id==4:
                    cv2.circle(img,(cx,cy),10,(255,0,255),cv2.FILLED)
            mpDraw.draw_landmarks(img,handLms,mpHands.HAND_CONNECTIONS)
     
    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime=cTime
    cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,
               (255,0,255),3)
    
    cv2.imshow("Image",img)
    cv2.waitKey(1)
    
    


import cv2
import mediapipe as mp
import time


cap=cv2.VideoCapture(0)
mpHands=mp.solutions.hands
hands=mpHands.Hands()
mpDraw=mp.solutions.drawing_utils


pTime=0
cTime=0
while True:
    success, img= cap.read()
    print(img)
    imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results=hands.process(imgRGB)
    
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id,lm in enumerate(handLms.landmark):
                #print(id,lm)
                h,w,c = img.shape     # height,weight and channells for image
                cx, cy = int(lm.x*w),int(lm.y*h)  # they are decimal places and converted into intergers (position of centered)
                #print(id,cx,cy)
                if id==4:
                    cv2.circle(img,(cx,cy),10,(255,0,255),cv2.FILLED)
            mpDraw.draw_landmarks(img,handLms,mpHands.HAND_CONNECTIONS)
     
    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime=cTime
    cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,
               (255,0,255),3)
    
    cv2.imshow("Image",img)
    cv2.waitKey(1)
    
    


import cv2
cap=cv2.VideoCapture(0)
sucess, img=cap.read()
print(img)
imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)



cap.release()
cv2.destroyAllWindows()


# In[ ]:





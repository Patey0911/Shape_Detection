import cv2
import numpy as np
img=cv2.VideoCapture(0)
ret, frame1=img.read()
while(True):
    ret, frame1=img.read()
    imgGrey=cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    _,thrash=cv2.threshold(imgGrey, 150, 255,cv2.THRESH_BINARY)
    contours,_=cv2.findContours(thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        approx=cv2.approxPolyDP(contour, 0.09* cv2.arcLength(contour, True), True)
        if (cv2.contourArea(contour)>1000 and cv2.contourArea(contour)<30000 and len(approx)>2):
            cv2.drawContours(frame1, [approx], 0, (0,0,255), 3)
            x=approx.ravel()[0]
            y=approx.ravel()[1]
            if(len(approx)==3):
                cv2.putText(frame1, 'Triunghi', (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (102, 255, 51), 2)
            elif(len(approx)==4):
                x ,y, w, h = cv2.boundingRect(approx)
                aspectRatio = float(w)/float(h)
                if aspectRatio >= 0.8 and aspectRatio <= 1.2:
                    cv2.putText(frame1, 'Patrat', (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (204, 0, 0), 2)
                else:
                    cv2.putText(frame1, 'Dreptunghi', (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 255), 2)
    cv2.imshow('video', frame1)
    ret, frame1 = img.read()
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break



cv2.destroyAllWindows()

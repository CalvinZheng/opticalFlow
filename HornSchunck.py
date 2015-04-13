import numpy as np
import cv2
import video
import sys

if __name__ == '__main__':
    import sys
    try: fn = sys.argv[1]
    except: fn = 0
    
cap = cv2.VideoCapture(fn)

ret,prevframe=cap.read()
prevgray=cv2.cvtColor(prevframe,cv2.COLOR_BGR2GRAY)
while(cap.isOpened()):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    sobely = cv2.Sobel(gray,cv2.CV_64F,0,1,ksize=-1)
    time_grad=gray-prevgray
    vy=-time_grad/sobely
    #abs_sobely = np.absolute(sobely)
    #sobel_8u = np.uint8(abs_sobely)
    #gradient_y=np.gradient(gray)

    #cv2.imshow('frame',sobely)
    #cv2.imshow('frame',time_grad)
    cv2.imshow('frame',vy)
    #print sobely[10:20,10:20]
    if cv2.waitKey(1) & 0xFF == ord('q'):
         break
    prevgray=gray

cap.release()
cv2.destroyAllWindows()
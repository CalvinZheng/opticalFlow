import numpy as np
import cv2
import video
import sys

if __name__ == '__main__':
    import sys
    try: fn = sys.argv[1]
    except: fn = 0
    
cap = cv2.VideoCapture(fn)

while(cap.isOpened()):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    sobely = cv2.Sobel(gray,cv2.CV_64F,0,1,ksize=-1)
    abs_sobely = np.absolute(sobely)
    sobel_8u = np.uint8(abs_sobely)
    gradient_y=np.gradient(gray)
    print gray[20:25,10:15]
    print sobely[20:25,10:15]
    cv2.imshow('frame',sobel_8u)
    if cv2.waitKey(1) & 0xFF == ord('q'):
         break

cap.release()
cv2.destroyAllWindows()
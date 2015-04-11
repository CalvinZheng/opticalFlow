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

    cv2.imshow('frame',sobely)
    print sobely[10:20,10:20]
    if cv2.waitKey(1) & 0xFF == ord('q'):
         break

cap.release()
cv2.destroyAllWindows()
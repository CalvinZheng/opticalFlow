#!/usr/bin/env python

import numpy as np
import cv2
import video
import PIL.Image as Image

help_message = '''
USAGE: opt_flow.py [<video_source>] [<int>f]

will output depth map calculated using f-th frame
'''

if __name__ == '__main__':
    import sys
    print help_message
    try: fn = sys.argv[1]
    except: fn = 0
    try: skip = int(sys.argv[2])
    except: skip = 0

    cam = video.create_capture(fn)
    for i in range(0,skip):
        ret, prev = cam.read()
    ret, prev = cam.read()
    prevgray = cv2.cvtColor(prev, cv2.COLOR_BGR2GRAY)
    show_hsv = False
    show_glitch = False
    cur_glitch = prev.copy()
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    flow = cv2.calcOpticalFlowFarneback(prevgray, gray, 0.5, 3, 15, 3, 5, 1.2, 0)
    magFlow = (np.sum(flow**2, axis=2))**0.5
    im = Image.fromarray(np.uint8(magFlow*255/magFlow.max()), mode="L")
    im.show()

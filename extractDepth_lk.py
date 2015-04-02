#!/usr/bin/env python

'''
Lucas-Kanade tracker
====================

Lucas-Kanade sparse optical flow demo. Uses goodFeaturesToTrack
for track initialization and back-tracking for match verification
between frames.

USAGE: extractDepth_lk.py [<video_source>] [<int>f]

will output depth map calculated using f-th frame
'''

import numpy as np
import cv2
import video
import scipy.interpolate
import PIL.Image as Image

lk_params = dict( winSize  = (15, 15),
                  maxLevel = 2,
                  criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

feature_params = dict( maxCorners = 1000,
                       qualityLevel = 0.3,
                       minDistance = 7,
                       blockSize = 7 )

class App:
    def __init__(self, video_src, skipFrame):
        self.track_len = 10
        self.detect_interval = 5
        self.tracks = []
        self.cam = video.create_capture(video_src)
        self.frame_idx = 0
        self.skipFrame = skipFrame

    def run(self):
        for i in range(0,self.skipFrame):
            ret, frame = self.cam.read()
        ret, frame = self.cam.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        ret, frame2 = self.cam.read()
        frame2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
        features = cv2.goodFeaturesToTrack(frame, **feature_params)
        p1, st, err = cv2.calcOpticalFlowPyrLK(frame, frame2, features, None, **lk_params)
        (h, w) = frame.shape
        grid_x, grid_y = np.mgrid[0:h, 0:w]
        values = ((p1-features)[:,0,0]**2+(p1-features)[:,0,1]**2)**0.5
        features.shape = (-1,2)
        grid_z0 = scipy.interpolate.griddata(features, values, (grid_y, grid_x), method='nearest', fill_value=0)
        im = Image.fromarray(np.uint8(grid_z0*255/grid_z0.max()), mode='L')
        im.show()

def main():
    import sys
    try: video_src = sys.argv[1]
    except: video_src = 0
    try: skipFrame = int(sys.argv[2])
    except: skipFrame = 100

    print __doc__
    App(video_src, skipFrame).run()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()

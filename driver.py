from moviepy.editor import *
from math import exp
import cv2
import numpy as np
import sys


#threshold = a*previous + b*mean + c*standard_deviation
a=float(sys.argv[1])
b=float(sys.argv[2])
c=float(sys.argv[3])
N= int(sys.argv[4]) # The size of the sliding window
K= int(sys.argv[5]) #The Number of Decay Frames
s=float(sys.argv[6]) # The Decay Parameter
mean=0
sd=0
previous=0
threshold = 0

clip = VideoFileClip(sys.argv[7]).subclip(0,120)

grey_frams=[]
images=[]
window=np.array(list())


for frames in clip.iter_frames():
    im=cv2.cvtColor(frames,cv2.COLOR_RGB2GRAY)
    images.append(im)
    gf=np.matrix(im)
    grey_frams.append(gf)

grey_frams=np.array(grey_frams)

window_index = 0
decay_phase=False
decay_frames=0

changes=0
for i in range(0,len(grey_frams)-1):
    SAD =  np.sum(np.sum(grey_frams[i+1]-grey_frams[i]))
    check=SAD

    if len(window) < N :
        decay_frames+=1
        window=np.insert(window,len(window),SAD)
        continue

    mean = np.mean(window)
    sd = np.std(window)

    if window_index!=0:
        previous= window[window_index-1]
    else:
        previous= window[-1]

    if decay_phase:
        decay_frames+=1
        #print 'check',check
        check = check * exp(-1*s*decay_frames)
        #print 'now', check
        if decay_frames == K:
            decay_phase=False

    threshold = a*previous +b*mean +c*sd
    print SAD,check,threshold
    if check > threshold:
        changes+=1
        decay_phase= True
        decay_frames=0
        cv2.imwrite("Scene"+str(changes)+".jpg",images[i])



    window[window_index]=SAD
    window_index= (window_index+1)%N
print 'Total Scene Changes Detected',changes

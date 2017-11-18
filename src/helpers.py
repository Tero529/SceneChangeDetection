from moviepy.editor import *
from math import exp
import cv2
import numpy as np

def parse(clipName):
    clip = VideoFileClip(clipName).subclip(0,120)
    grey_frams=[]
    images=[]
    window=np.array(list())

    for frames in clip.iter_frames():
        im=cv2.cvtColor(frames,cv2.COLOR_RGB2GRAY)
        images.append(im)
        gf=np.matrix(im)
        grey_frams.append(gf)
    grey_frams=np.array(grey_frams)

    return (grey_frams,images)

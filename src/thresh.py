from math import exp
import cv2
import numpy as np

#threshold = a*previous + b*mean + c*standard_deviation

#N The size of the sliding window
#K The Number of Decay Frames
#s The Decay Parameter


def detect(grey_frams,images,a,b,c,N,K,s):
    mean=0
    sd=0
    previous=0
    threshold = 0

    window=np.array(list())
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
            if len(window)==1:
                continue

        mean = np.mean(window)
        sd = np.std(window)

        if len(window)<N:
            previous=window[-2]
        elif window_index!=0:
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
        if len(window)<N:
            continue


        window[window_index]=SAD
        window_index= (window_index+1)%N
    return changes

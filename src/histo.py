from math import exp
from math import sqrt
import cv2
import numpy as np
from pylab import *
import csv

def detect(grey_frams):
    coorelations = []
    reference =[]
    numbers=[]
    for i in range(0,len(grey_frams)):
        gram = makeHisto(grey_frams[i])
        if i==0:
            reference = gram
            mean= np.mean(gram)
        else:
            coor= coorelation(reference,gram,mean)
            coorelations.append([i+1,coor])
            print coor


    #plot(x_axis,coorelations)
    #print coorelations
    return coorelations



def coorelation(reference,frame,mean):
    mean_fr = mean
    mean_i = mean
    numerator=0
    denominator_fr = 0
    denominator_i = 0
    for j in range(len(reference)):
        numerator = numerator + (reference[j] - mean_fr)*(frame[j] - mean_i)
        denominator_fr = denominator_fr + (reference[j] - mean_fr)*(reference[j] - mean_fr)
        denominator_i = denominator_i + (frame[j] - mean_i)*(frame[j] - mean_i)

    denominator = sqrt(denominator_i*denominator_fr)
    coor = numerator/denominator
    return coor


def makeHisto(grey_frame):
    histogram = [0] * 256
    for i in range(len(grey_frame)):
        for j in range(len(grey_frame[i])):
            histogram[grey_frame[i][j]]+=1
    return histogram

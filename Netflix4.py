'''
Combines movieMeans and customerMeans

modified for Netflix Project part 4
'''

import os
import sys
from math import sqrt

probeFile = sys.argv[1]
actualRatingsFile = sys.argv[2]
customerMeansFile = sys.argv[3]
movieMeansFile = sys.argv[4]

bias = 3.604289964420661                                                        # Calulated from Overall Means

cmeans = {}
mmeans = {}
cratings = []                                                                   # The values from cmeans in the same order as probe.txt
mratings = []
aratings = []
combined = []

def main():
    cmeans   = populateCustomer()
    mmeans   = populateMovie()

    aratings = populateActual()
    cratings = orderCustomer()
    mratings = populatePredicted()

    cmultiplier = .8                                                            # this cmultiplier and mmultiplier combo was found to produce
    mmultiplier = .2                                                            # the smallest rvalue. Tests can be found in rtests.txt
    combined = combineRatings(cmultiplier, mmultiplier)
    
    print("RMSE = " + str(rmse(aratings, combined)))

def populateCustomer():                                                         # Populate the cmeans array to be the same order as probe.txt
    with open(customerMeansFile) as f:
        for line in f:
            split = line.split(":")
            k = int(split[0])                                                   # UID
            v = float(split[1][:-1])                                            # Average rating
            cmeans[k] = v
    return cmeans

def orderCustomer():
    with open(probeFile) as probe:
        for line in probe:
            if not ":" in line:
                value = int(line[:-1])
                cratings.append(cmeans[value])
    return cratings

def populateMovie():
    with open(movieMeansFile) as movie:
        for line in movie:
            split = line.split(":")
            MID = split[0]
            rating = split[1][:-1]
            mmeans[int(MID)] = float(rating)
    return mmeans

def populateActual():
    with open(actualRatingsFile) as f:
        for line in f:
            value = int(line[:-1])
            aratings.append(value)
    return aratings

def populatePredicted():
    with open(probeFile) as probe:
        for line in probe:
            if ":" in line:
                MID = int(line.split(":")[0])
            else:
                mratings.append(mmeans[MID])
    return mratings

def combineRatings(cmultiplier, mmultiplier):
    for i in range(0, len(cratings)):
        cvalue = cratings[i] * cmultiplier
        mvalue = mratings[i] * mmultiplier
        combined.append(cvalue + mvalue)
    return combined

def rmse(actual, predicted):
    difference = []
    for x in range(0, len(actual)):
        difference.append((actual[x] - (predicted[x] + bias)) ** 2)             # Add bias back in 
    avg = sum(difference) / len(difference)
    return sqrt(avg)

main()

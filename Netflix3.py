'''
Predict using movieMeans.txt
'''

import os
import sys
from math import sqrt

probeFile = sys.argv[1]
actualRatingsFile = sys.argv[2]
movieMeansFile = sys.argv[3]

mmeans = {}
aratings = []
mratings = []

def main():
    mmeans = populateMovie()
    aratings = populateActual()
    mratings = populatePredicted()
    print("RMSE = " + str(rmse(aratings, mratings)))

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

def rmse(actual, predicted):
    difference = []
    for x in range(0, len(actual)):
        difference.append((actual[x] - predicted[x]) ** 2)
    avg = sum(difference) / len(difference)
    return sqrt(avg)

main()

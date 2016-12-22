import sys
import os
from math import sqrt

probeFile = sys.argv[1]
actualRatings = sys.argv[2]
customerMeans = sys.argv[3]

cmeans = {}
cratings = []                                                                   # The values from cmeans in the same order as probe.txt
aratings = []

def main():
    orderCustomer(populateCustomer(customerMeans, cmeans), cratings)
    populateActual(actualRatings, aratings)
    print("RMSE = " + str(rmse(aratings, cratings)))
 

def populateCustomer(customerMeans, cmeans):                                    # Populate the cmeans array to be the same order as probe.txt
    with open(customerMeans) as f:
        for line in f:
            split = line.split(":")
            k = int(split[0])                                                   # UID
            v = float(split[1][:-1])                                            # Average rating
            cmeans[k] = v
    return cmeans


def orderCustomer(cmeans, cratings):
    with open(probeFile) as probe:
        for line in probe:
            if not ":" in line:
                value = int(line[:-1])
                cratings.append(cmeans[value])
    return cratings


def populateActual(actualRatings, aratings):
    with open(actualRatings) as f:
        for line in f:
            value = int(line[:-1])
            aratings.append(value)
    return aratings


def rmse(actual, predicted):
    difference = []
    for x in range(0, len(actual)):
        difference.append((actual[x] - predicted[x]) ** 2)
    avg = sum(difference) / len(difference)
    return sqrt(avg)

main()

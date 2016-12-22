'''
Reads through actualRatings.txt and uses the values to check predicted ratings
and generates a RMSE
'''

import sys
import os
from math import sqrt

probeFile = sys.argv[1]
ratings = sys.argv[2]

mean = 3.604289964420661                                                        # Calculated mean from OverallMean.py

actualRatings = []
predictedRatings = []

with open(ratings) as actual:
    for line in actual:
        actualRatings.append(int(line[0:1]))

with open(probeFile) as probe:
    for line in probe:
        if not ":" in line:                                                     # Ignore lines with a movie ID
            predictedRatings.append(mean)

def rmse(actual, predicted):
    difference = []
    for x in range(0, len(actual)):
        difference.append((actual[x] - predicted[x]) ** 2)
    return sqrt(sum(difference)/len(difference))

print("RMSE =",rmse(actualRatings, predictedRatings))

'''
Reads through actualRatings.txt and uses the values to check predicted ratings
and generates a RMSE
'''

import os
from math import sqrt

mean = 3.604289964420661 # Calculated mean from AllMean.py

actualRatings = []
predictedRatings = []

with open("actualRatings.txt") as actual:
    for line in actual:
        actualRatings.append(int(line[0:1]))

with open("../netflix-data/probe.txt") as probe:
    for line in probe:
        if not ":" in line: # Ignore lines with a movie ID
            predictedRatings.append(mean)

def rmse(actual, predicted):
    difference = []
    for x in range(0, len(actual)):
        difference.append((actual[x] - predicted[x]) ** 2)
    return sqrt(sum(difference)/len(difference))

print(rmse(actualRatings, predictedRatings))

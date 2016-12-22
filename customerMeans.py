'''
reads all 17770 movie files and computes the average for each
customer and prints to customerMeans.txt in the format
[userID]:[avgRating]

modified for Netflix Project part 4
'''

import sys
import os
from collections import defaultdict

directory = sys.argv[1]

bias = 3.604289964420661                                                        # Equivilent to the Overall Means value

customerRatings = defaultdict(list)
customerMeans   = {}

def main():
    filelist = getDirecotryList(directory)
    customerRatings = populateCustomerRatings(filelist)
    customerMeans   = populateCustomerMeans(customerRatings, bias)
    writeMeans()

def getDirecotryList(directory):
    filelist = []
    for f in os.listdir(directory):
        filelist.append(f)
    filelist.sort()
    return filelist

def populateCustomerRatings(filelist):
    for f in filelist:
        with open(directory + "/" + f) as movie:
            movie.readline()                                                    # Skip movieID line
            for line in movie:
                split = line.split(",")
                UID = split[0]
                rating = int(split[1]) - bias                                   # Remove bias
                customerRatings[UID].append(rating)
    return customerRatings

def populateCustomerMeans(customerRatings, bias):
    for k, v in customerRatings.items():
        avgRating = sum(v)/len(v)
        customerMeans[k] = avgRating
    return customerMeans

def writeMeans():
    with open("customerMeans.txt", 'w') as f:
        for k, v in customerMeans.items():
            f.write(k + ":" + str(v) + "\n")

main()

''' 
Grabs the average user rating for each movie and prints it out to 
movieMeans.txt in the form [MID]:[averageRating]

modified for Netflix Project part 4
'''

import sys
import os

bias = 3.604289964420661                                                        # Equivilent to the Overall Means value

directory = sys.argv[1]

filelist    = []
movieMeans  = []
unbiasMeans = []

def main():
    filelist = getDirecotryList()
    movieMeans = populateMovieRatings(filelist)
    unbiasMeans = removeBias(bias)
    writeMeans()

def getDirecotryList():
    for f in os.listdir(directory):
        filelist.append(f)
    filelist.sort()
    return filelist

def getAvgRating(movie):
    ratingsArray = []
    movie.readline()                                                            # Skip the first line (movieID)
    for line in movie:
        rating = int(line.split(",")[1])
        ratingsArray.append(rating)
    return sum(ratingsArray)/len(ratingsArray)

def populateMovieRatings(filelist):
    for f in filelist:
        with open(directory + "/" + f) as movie:
            movieMeans.append(getAvgRating(movie))
    return movieMeans

def removeBias(bias):
    for value in movieMeans:
        unbiasMeans.append(value - bias)

def writeMeans():
    with open("movieMeans.txt", 'w') as f:
        for i in range(0, len(unbiasMeans)):
            f.write(str(i + 1) + ":" + str(unbiasMeans[i]) + "\n")

main()

'''
Reads through probe.txt and finds the matching userID for each movieID
and then prints out the ratings to actualRatings.txt in the same order as the
probe.txt file
'''

import sys
import os
import io

trainingSet = sys.argv[1]
probeFile = sys.argv[2]

ratings = {}
movie = None
outputArray = []

# Create an ordered list of the filenames in the training set 
files = []
for filename in os.listdir(trainingSet):
    files.append(trainingSet + '/' + filename)
files.sort()

# Parse through probe.txt adding ratings that match the userID to the ratings list
with open(probeFile) as probe:
    for line in probe:
        if ":" in line:
            movie = open(files[int(line[:-2]) - 1])                             # Open the movie file by referencing the files list
            movie.readline()                                                    # Skip the line with the movieID   
        else:
            for curLine in movie:
                UID = curLine.split(',')[0]                                     # Grabs the userID  
                if int(UID) == int(line[:-1]):
                    rating = curLine.split(',')[1]
                    ratings[line] = int(rating)                                 # add UID:rating to the dictionary
                    break

# Order the output to match the order probeFile
with open(probeFile) as probe:
    for line in probe:
        if not ":" in line:
            outputArray.append(ratings[line])           

# Print the array to actualRatings.txt
with open('actualRatings.txt', 'w') as output:
    for item in outputArray:
        output.write(str(item) + "\n")

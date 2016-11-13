'''
Reads through probe.txt and finds the matching userID for each movieID
and then prints out the ratings to actualRatings.txt 
'''

import os
import io

# Create an ordered list of the filenames in the training set 
files = []
for filename in os.listdir('../netflix-data/training_set'):
    files.append("../netflix-data/training_set/" + filename)
files.sort()

ratings = []
movie = None

# Parse through probe.txt adding ratings that match the userID to the ratings list
with open('../netflix-data/probe.txt') as probe:
    for line in probe:
        if ":" in line:
            movie = open(files[int(line[:-2]) - 1])   # Open the movie file by referencing the files list
            movie.readline()    # Skip the line with the movieID   
        else:
            for curLine in movie:
                raterID = curLine.split(',')[0]     # Grabs the userID
                if int(raterID) == int(line[:-1]):
                    rating = curLine.split(',')[1]
                    ratings.append(int(rating))
                    break

# Print the array to actualRatings.txt
output = open('actualRatings.txt', 'w')
for item in ratings:
    output.write("%i\n" % item)
output.close()

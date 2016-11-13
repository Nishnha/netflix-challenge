'''
Calculates a mean of all ratings for all movies in the training set
'''

import os

total = 0
cardinality = 0

for filename in os.listdir("../netflix-data/training_set"):
    with open("../netflix-data/training_set/" +  filename) as f:
        f.readline() # Skip the first line (movie number)
        for line in f:
            rating = line.split(',')[1] # Select the rating only
            total = total + int(rating)
            cardinality = cardinality + 1

print("Overall Mean = ", total / float(cardinality))

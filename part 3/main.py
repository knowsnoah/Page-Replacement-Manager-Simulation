#Part 3 
#Testing the three algorithm implemented in Part 2 of the project.

#importing the three algorithms from their respective files
from implementation.fifo import fifo
from implementation.lru import lru
from implementation.opt import opt

import random

#function to generate testing data for the three algorithms
#creating a file with random reference strings of pages (0-7) with a specified length and number of strings
def generateTestingData(filename="TestingData.txt", numStrings=50, stringLength=30):
    with open(filename, "w") as file:
        for _ in range(numStrings):
            referenceString = ""

            for _ in range(stringLength):
                page = random.randint(0, 7)
                referenceString += str(page)

            file.write(referenceString + "\n")

def generate_average():
    return

if __name__ == "__main__":
    generate_average()
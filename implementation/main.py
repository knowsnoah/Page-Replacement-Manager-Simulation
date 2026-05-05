#Part 3 
#Testing the three algorithm implemented in Part 2 of the project.

#importing the three algorithms from their respective files
from fifo import fifo
from lru import lru
from opt import opt

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


#this function reads the testing data from the file and returns it as a list of referenceStrings
def readTestingData(filename="TestingData.txt"):
    referenceStrings = []
    with open(filename, "r") as file:
        for line in file:
            referenceStrings.append([int(x) for x in line.strip()])
    return referenceStrings


#function that will calculate the average number of page faults for each algorithm based on the testing data generated
def generate_average():
    # read all reference strings
    referenceStrings = []

    #opens the testing data file and reads each line
    with open("TestingData.txt", "r") as file:
        for line in file:
            referenceStrings.append([int(x) for x in line.strip()])

    frameSizes = [3, 4, 5, 6]

    #printing the average page faults for each algorithm and its corresponding frame size in a formatted table
    print("\nAverage Page Faults:\n")
    print(f"{'Frames':<10}{'FIFO':<15}{'LRU':<15}{'OPT':<15}")
    print("-" * 50)

    for frameSize in frameSizes:
        fifo_total = 0
        lru_total = 0
        opt_total = 0

        for ref in referenceStrings:
            fifo_total += fifo(ref, frameSize)
            lru_total += lru(ref, frameSize)
            opt_total += opt(ref, frameSize)

        n = len(referenceStrings)

        fifo_avg = fifo_total / n
        lru_avg = lru_total / n
        opt_avg = opt_total / n

        print(f"{frameSize:<10}{fifo_avg:<15.2f}{lru_avg:<15.2f}{opt_avg:<15.2f}")


if __name__ == "__main__":
    generateTestingData()
    print("Testing data generated in 'TestingData.txt'.")

    generate_average()
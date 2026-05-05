#Testing the three algorithms implemented in Part 2 of the project.

#importing the three algorithms from their respective files
from fifo import fifo
from lru import lru
from opt import opt


if __name__ == "__main__":
    #referenceString used in the example for Part 1
    referenceString = [ 0, 1, 2, 3, 0, 1, 2, 4, 0, 1, 2, 5, 0, 1, 2, 6, 0, 1, 2, 3, 0, 1, 2, 4, 0, 1, 2, 5, 0, 1]
    frameSizes = [3, 4, 5, 6]

    expected = {
        3: (30, 30, 16),
        4: (19, 10, 10),
        5: (16, 10, 9),
        6: (13, 10, 8)
    }

    #printing the header 
    print(f"{'Frame Size':<12}{"fifo Faults":<12}{"lru Faults":<12}{"opt Faults":<12}")
    
    #looping throught the frame sizes and calculating the page faults for each algorithm, then comparing it to the expected values
    #and printing the results in a formatted table
    for i, frameSize in enumerate(frameSizes, start=1):
        fifoFaults = fifo(referenceString, frameSize)
        lruFaults = lru(referenceString, frameSize)
        optFaults = opt(referenceString, frameSize)

        exp_fifo, exp_lru, exp_opt = expected[frameSize]

        check = "√" if (fifoFaults, lruFaults, optFaults) == expected[frameSize] else "X"
        
        print(f"{frameSize:<12}{fifoFaults:<12}{lruFaults:<12}{optFaults:<12}{check}")
        print()
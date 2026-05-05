# Part 2
# implementation of FIFO page replacement algorithm

from collections import deque

#function
def fifo(referenceString, frameSize):
    #initialize variables
    frames = []
    queue = deque()
    pageFaults = 0
    
    #looping through the referenceString
    for page in referenceString:
        #check if the page is already in the frames
        if page in frames:
            continue
        #if the page is not in the frames, we have a page fault
        else:
            pageFaults += 1 #increment page faults

            #if there is still space in the frames, add the page to frames and queue
            if len(frames) < frameSize:
                frames.append(page)
                queue.append(page)
            #if there is no space, then we need to remove the oldest page and add the new page
            else:
                removedPage = queue.popleft()
                frames.remove(removedPage)

                frames.append(page)
                queue.append(page)
    
    #returning the number of page faults
    return pageFaults


if __name__ == "__main__":
    #referenceString used in the example for Part 1
    referenceString = [ 0, 1, 2, 3, 0, 1, 2, 4, 0, 1, 2, 5, 0, 1, 2, 6, 0, 1, 2, 3, 0, 1, 2, 4, 0, 1, 2, 5, 0, 1]
    frameSize = 3
    pageFaults = fifo(referenceString, frameSize)
    print(f"Number of page faults: {pageFaults}")


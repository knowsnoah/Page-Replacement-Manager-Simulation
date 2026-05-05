#Part 2
#implementation of LRU page replacement algorithm

from collections import deque

#function
def lru(referenceString, frameSize):
    #initialize variables
    frames = []
    lastUsed = {}
    pageFaults = 0

    #looping throuhgh the referenceString
    for i, page in enumerate(referenceString):
        #if the page is in frames, we update the last step it was used (i)
        if page in frames:
            lastUsed[page] = i
        else:
            #if the page is not in frames, we have a page fault
            pageFaults += 1

            #if there is space in frames add the page
            #otherwise, we remove the least recently used page using its dictionary value, then add the new page with its last used step (i)
            if len(frames) < frameSize:
                frames.append(page)
            else:
                lru_page = min(frames, key=lambda p: lastUsed[p])
                frames.remove(lru_page)
                frames.append(page)

            lastUsed[page] = i

    #returning the number of page faults
    return pageFaults


if __name__ == "__main__":
    #referenceString used in the example for Part 1
    referenceString = [ 0, 1, 2, 3, 0, 1, 2, 4, 0, 1, 2, 5, 0, 1, 2, 6, 0, 1, 2, 3, 0, 1, 2, 4, 0, 1, 2, 5, 0, 1]
    frameSize = 5
    pageFaults = lru(referenceString, frameSize)
    print(f"Number of page faults: {pageFaults}")


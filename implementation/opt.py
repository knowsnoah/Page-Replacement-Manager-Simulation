#Part 2
#implementation of optimnal page replacement algorithm

#function
def opt(referenceString, frameSize):
    #initalized variables
    frames = []
    pageFaults = 0

    #looping through the referenceString (index, page)
    for i, page in enumerate(referenceString):
        #if the page is in frames, we continue
        if page in frames:
            continue
        
        pageFaults += 1

        if len(frames) < frameSize:
            frames.append(page)
        else:
            removedPage = None
            farthestUse = -1

            for p in frames:
                try:
                    nextUse = referenceString[i + 1:].index(p) + i + 1
                except ValueError:
                    removedPage = p
                    break

                if nextUse > farthestUse:
                    farthestUse = nextUse
                    removedPage = p

            indexToReplace = frames.index(removedPage)
            frames[indexToReplace] = page

    return pageFaults




if __name__ == "__main__":
    #referenceString used in the example for Part 1
    referenceString = [ 0, 1, 2, 3, 0, 1, 2, 4, 0, 1, 2, 5, 0, 1, 2, 6, 0, 1, 2, 3, 0, 1, 2, 4, 0, 1, 2, 5, 0, 1]
    frameSize = 3
    pageFaults = opt(referenceString, frameSize)
    print(f"Number of page faults: {pageFaults}")

def maxInRange(someList, start, end):
    maxVal = someList[start]
    for x in range(start, end + 1):
        if(someList[x] > maxVal):
            maxVal = someList[x]
    return maxVal

def minInRange(someList, start, end):
    minVal = someList[start]
    for x in range(start, end + 1):
        if(someList[x] < minVal):
            minVal = someList[x]
    return minVal

def elementCounter(someList, element):
    counter = 0
    for x in someList:
        if(element == x):
            counter += 1
    return counter

def elementPos(someList, element):
    pos = []
    currentPos = 0
    for x in range(len(someList)):
        if(someList[x] == element):
            pos.append(x)
    return pos

def ranges(sortedList):
    rangeList = []
    if(sortedList == rangeList):
        return sortedList
    else:
        start = sortedList[0]
        end = sortedList[0]
        for x in range(len(sortedList) - 1):
            if(sortedList[x] + 1 == sortedList[x+1]):
                end = sortedList[x+1]
            else:
                rangeList.append((start,end))
                start = sortedList[x+1]
                end = sortedList[x+1]
        rangeList.append((start,end))
    return rangeList


def occupySlot(sequence):
    length = len(sequence) - 2
    for x in range(length):
        if(sequence[x] == 1 and sequence [x+1] == 0 and sequence [x+2] == 0):
            sequence[x+2] = 1

        elif(sequence[x] == 0 and sequence [x+1] == 0 and sequence [x+2] == 1):
            sequence[x] = 1

        elif(sequence[x] == 0 and sequence [x+1] == 0 and sequence [x+2] == 0):
            sequence[x] = 1
            sequence[x+2] = 1
    #If the first index is one skip forward two otherwise check if the next index is 0 if it is place a person in the first index
    return sequence

def setMismatch(someList):
    for x in range(len(someList) - 1):
        if(someList[x] + 1 != someList[x+1]):
            return (someList[x+1], someList[x] + 1)


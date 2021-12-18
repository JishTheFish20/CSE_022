def heading(title, max_width=80, min_padding=4):
    titleLength = len(title) # gets length of the title
    overallLength = 2 + titleLength + min_padding*2 # checks the entire length of the header before we add any extra padding
    newPadding = (max_width - overallLength) // 2 # checks how much padding needs to be added to the header
    remainder = (max_width - overallLength) % 2 # checks if the header is odd

    if(overallLength > max_width): # if our title is longer then the space we have then we will shorten it
        for x in range(1,titleLength):
            titleLength = len(title[:-x]) #does not look at last letter in title
            overallLength = 2 + titleLength + min_padding*2

            if((overallLength + 3) == max_width): #checks if the changed length is shortend enough to add ellipses
                title = ("-"*min_padding + " " + title[:-x] + "..." + " " + "-"*min_padding)
                break

    elif(title == ""): # if we have no title then add no spaces
        title = ("-"*(newPadding+min_padding+1) + title + "-"*(newPadding+min_padding+1))
    else: # if our title is shorther then the total space then add more padding to make it fill up the space
        title = ("-"*(newPadding+min_padding) + " " + title + " " + "-"*(newPadding+min_padding + remainder))
    return title

def summarizeFines(fines):
    fineHolder = {}
    payment = 0
    newFines = []
    
    for x in range(len(fines)):
        if(fines[x][0] in fineHolder): # check to see if the name is already in the dictionary
            fineHolder[fines[x][0]] = fineHolder[fines[x][0]] + fines[x][1] #add the payment to a previous
            payment = 0 
        else:
            fineHolder[fines[x][0]] = fines[x][1] #add a new key and value to dictionary

    for x in fineHolder: #convert dictionary to list
        newFines.append([x,fineHolder[x]])

    return newFines

def findHighestDebtor(debts):
    fineHolder = {}
    payment = 0
    newDebts = []
    maxDebator = debts[0][0]

    for x in range(len(debts)):
        if(debts[x][0] in fineHolder): # check to see if the name is already in the dictionary
            payment = fineHolder[debts[x][0]] + debts[x][1] #add the payment to a previous 
            fineHolder[debts[x][0]] = payment
        else:
            fineHolder[debts[x][0]] = debts[x][1] #add a new key and value to dictionary

        if(fineHolder[maxDebator] < fineHolder[debts[x][0]]): # check to see if the current 
            maxDebator = debts[x][0]

    return maxDebator

def optimizeContainer(limit, customerList):
    bestPair = (customerList[0][0],customerList[1][0]) #set first pair as the best pair
    bestCost = customerList[0][1] + customerList[1][1] # set the first cost as the best cost

    for y in range(len(customerList) - 1): #for loop for checking each pair using two pointers
        for x in range(y , len(customerList) - 1): #starts from y going to 1 minus the end of the customer list
            if(limit >= (customerList[y][1] + customerList[x+1][1]) >= bestCost or bestCost > limit): # Does the current pair give a greater value then the last greatest value which also does not exceed the limit
                bestCost = customerList[y][1] + customerList[x+1][1]
                bestPair = (customerList[y][0],customerList[x+1][0])

    return bestPair

def dropLowestGrade(filename):
    students = []
    adjustedGrades = []
    i = 0

    f = open(filename, "r")
    lines = f.readlines()
    f.close()

    for x in range(len(lines)):
        students.append(lines[x].strip())

    for x in range(len(lines)):
        values = students[x].split(",")
        names = values[0]
        grade1 = values[1]
        grade2 = values[2]
        grade3 = values[3]
        if(grade1 < grade2 and grade1 < grade3):
            values.pop(1)
        elif(grade2 < grade1 and grade2 < grade3):
            values.pop(2)
        else:
            values.pop(3)
        adjustedGrades.append((names, [int(values[1]),int(values[2])]))
    return adjustedGrades

def averageGrade(gradeList):
    adjustedGrades = []
    for x in range(len(gradeList)):
        averageGrade = (list(gradeList)[x][1][0]+list(gradeList)[x][1][1])/2
        adjustedGrades.append((list(gradeList)[x][0], averageGrade))
    return adjustedGrades
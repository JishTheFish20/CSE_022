def countVowels(s):
    vowels = ["a", "e", "i", "o", "u"]
    word = []
    word[:0] = s.lower()
    totalVowels = 0
    for x in word:
        for y in vowels:
            if(x == y):
                totalVowels += 1
    return totalVowels

def isStable(s):
    i = 0
    a = " "
    b = " "
    word = []
    word2 = []
    word[:0] = s

    if(len(word) % 2 != 0):
        word.pop((len(word) // 2))

    middle = len(word) //2

    firstHalf = word[:middle]
    secondHalf = word[middle:]

    print(firstHalf)
    print(secondHalf)

    for ele in firstHalf: 
        a += ele
    
    for ele in secondHalf: 
        b += ele

    print(a,b)
    
    if(countVowels(a) == countVowels(b)):
        return True
    else: 
        return False

def hasDoubleLetters(s):
    word = []
    word[:0] = s.lower()
    startPointer = 0
    endPointer = 1

    while(endPointer < len(s)):
        if(word[startPointer] == word[endPointer]):
            return True
        startPointer += 1
        endPointer += 1
    return False

def interleave(word1, word2):
    a = ""
    wordOneArray = []
    wordOneArray[:0] = word1
    print(word1)

    wordTwoArray = []
    wordTwoArray[:0] = word2
    print(word2)

    i = 0
    k = 1

    combinedArray = []

    length = max(len(wordOneArray), len(wordTwoArray))
    
    if(len(wordTwoArray) == 0):
        combinedArray = wordOneArray
        print(combinedArray)
    
    elif(len(wordOneArray) == 0):
        combinedArray = wordTwoArray
        print(combinedArray)
    
    else:

        for x in range(length):

            if(x <= len(wordOneArray)):
                print(wordOneArray[x])
                combinedArray.insert(i,wordOneArray[x])
            if(x < len(wordTwoArray)):
                combinedArray.insert(k,wordTwoArray[x])
            
            print(combinedArray)
            i += 2
            k += 2

    for ele in combinedArray: 
        a += ele
    print(a)

    return a

def lcp(s1, s2):
    wordOneArray = []
    wordOneArray[:0] = s1.lower()
   

    wordTwoArray = []
    wordTwoArray[:0] = s2.lower()

    prefix = ""
    hasPrefix = None

    length = min(len(wordOneArray), len(wordTwoArray))
    if(wordOneArray[0] != wordTwoArray[0]):
        prefix = ""
    else:

        for x in range(length):
            if(wordOneArray[x] == wordTwoArray[x]):
                prefix += wordOneArray[x]
    return(prefix)

def extractLastName(full_name, email):
    lastName = ""

    nameArray = []
    nameArray[:0] = full_name.lower()
   

    emailArray = []
    emailArray[:0] = email.lower()
    emailArray.pop(0)

    upperCase = True
    
    for x in range(13):
        emailArray.pop(len(emailArray)-1)
        print(emailArray)

    length = len(emailArray)

    while(nameArray[0] != " " or emailArray[0] != nameArray[1]):
        print(nameArray)
        nameArray.pop(0)
    nameArray.pop(0)
            
    for ele in nameArray: 
        if(ele == " " or ele == "-"):
            upperCase = True
            lastName += ele
            next
        elif(upperCase == True):
            lastName += ele.upper()
            upperCase = False
        else:
            lastName += ele
    return(lastName)


    




    


        

   

        

if __name__ == "__main__": # Only do the following if this file is called direfctly
    
   # year = int(input("Leap year: "))

    answer = extractLastName( "Steve Jobs","sjobs@ucmerced.edu") == "Jobs"

    print(answer)



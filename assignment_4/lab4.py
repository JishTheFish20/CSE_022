def simple_lock(x1, x2, x3, y1, y2, y3):
    currentCombo = [x1, x2, x3]
    openCombo = [y1, y2, y3]
    increment = 0

    for j in range(len(currentCombo)):
        test1 = abs(currentCombo[j] - openCombo[j]) #turn left
        test2 = abs(openCombo[j] - currentCombo[j]) #turn right

        if(currentCombo[j] == 9 and openCombo[j] < 5): #test to see if the current combo is 9 and its easier to turn left
            increment += openCombo[j]
      
        elif(openCombo[j] == 9 and currentCombo[j] < 5): #test to see if the open combo is 9 and its easier to turn right
            increment += currentCombo[j]
            
        elif(test1 <= test2): #checks if turning left or right is better
            increment += test1
            
        else:
            increment += test2

    return(increment)


    # min(x-y, 9-x+y)
    # min(y-x, 9-y+x)

def combo_lock(current, unlock):

    #takes a integer and splits it into digits which then are stored in a array
    currentCombo = [int(a) for a in str(current)]
    openCombo = [int(b) for b in str(unlock)]

    increment = 0

    for j in range(len(currentCombo)):
        test1 = abs(currentCombo[j] - openCombo[j]) #turn left
        test2 = abs(openCombo[j] - currentCombo[j]) #turn right

        # if currentCombo[j] < 5 and (openCombo[j]) > (6 + (currentCombo[j] + 5)): #test to see if the open combo is 9 and its easier to turn right
        #     increment += currentCombo[j]
        #     print(increment)

        if (currentCombo[j] > 5 and openCombo[j] < 5) and (openCombo[j]) < (2 + (openCombo[j] - 1)): #test to see if the open combo is 9 and its easier to turn right
            increment += (9 - currentCombo[j]) + (openCombo[j])
            print(increment)

        elif (currentCombo[j] < 5 and openCombo[j] > 5) and (openCombo[j]) >= (6 + (currentCombo[j] - 1)): #test to see if the open combo is 9 and its easier to turn right
            increment += (9 - openCombo[j]) + (currentCombo[j])
            print(increment)
        
        elif(test1 <= test2): #checks if turning left or right is better
            increment += test1
            
        else:
            increment += test2

    return(increment)

def is_perfect(n):
    nums = 0
    i = 1
    if(n % 2 != 0): # if n is odd return false
        return False
    
    for i in range(n-1): # take the given number and divide it by all its previous numbers and add them together
        i = i+1
        if(n%i == 0):
            nums += i
            print(nums)

    if(nums == n): # check if nums is equal to your number if it is then you have a perfect number
        return(True)
    else:
        return(False) 

def next_perfect(n):
    x = n + 1 # go to the next positive number after n
    while(is_perfect(x) != True): # check if your new number is a perfect number
        x += 1 # go to next positive number
        print(x)
    return(x)

def is_prime(x):
    if(x == 1):
        return False

    for i in range(2,x):
        if(x % i == 0):
            return(False)
    return True

def next_prime(n):
    x = n+1                     # goes to the next number after n
    while(is_prime(x) != True): #checks if x is prime
        x += 1                  #goes to the next number
        if(x % 2 == 0):         # if even add one 
            x +=1
    return(x)

def is_power(number, base):
    n = 0       #set exponent to 0
    x = base**n     #check to see what the base to the expoenet equal
    while(x != number and x < number):      # base to the exponent does not equal number then go to the next exponenet
        n +=1
        x = base**n
        print(x,number)
        if(x > number):     # if the base to the exponent is greater then the number the base is not a power of the number
            return(False)
    return(True)

def gcd(a, b):
    if (b == 0):
        return a
    return gcd(b, a % b)

def coprime(x, y):
    if (gcd(x,y) == 1):
       return (True)
    else:
        return(False)
    
def phi(n):
    x = n-1 # set x = 1 less then n
    totalCoPrimes = 0 # start at zero coprimes

    while(x > 0):  #check every number less then n
        if(coprime(n,x) == True): # check if this current iteration is a coprime and add one if it is
            totalCoPrimes += 1 
        x -= 1                     # go to the next number
    return totalCoPrimes

def sqrt(a, x, epsilon):
    while(abs(a/x - x) > epsilon): #checks to see if the diffrence of (a/x) and x is less then the ellipsion value
        x = ((x)+(a/x))/2 # go to the next root aproximation
    return(x)




        


if __name__ == "__main__": # Only do the following if this file is called direfctly
    
   # year = int(input("Leap year: "))

    answer = phi(9)

    print(answer)
            



     
 


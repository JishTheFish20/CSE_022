def wages(hours, rate):
    if hours > 40:
        return((40*rate) + (hours - 40)*(rate*1.5))
    else:
        return(hours*rate)

def canDonateBlood(donor, recipient):
    if ((donor == "A") or (donor == "B")) and ((recipient == "AB") or (recipient == donor)) :
        return(True)
    elif donor == recipient:
        return(True)
    elif donor == "O":
        return(True)
    else:
        return(False)

def leap(year):

    if (year%4 == 0) and (year%100 != 0):
        return(True)
    elif (year%400 == 0):
        return(True)
    else:
        return(False)

def daysInMonth(month, year):
    monthWithThirtyDays = [4,6,9,11]
    monthWithThirtyOneDays = [1,3,5,7,8,10,12]

    if ((leap(year) == True) and (month == 2)):
        return(29)
    elif(month in monthWithThirtyDays):
        return(30)
    elif(month in monthWithThirtyOneDays):
        return(31)
    else:
        return(28)

def pointInRect (x, y, rx, ry, rw, rh):

    rx2 = rx + rw
    ry2 = ry - rh

    if((rx <= x <= rx2) and (ry2 <= y <= ry)):
        return(True)
    else:
        return(False)

def rectInRect(x1, y1, w1, h1, x2, y2, w2, h2):
    rx1 = x1 + w1
    ry1 = y1 - h1

    rx2 = x2 + w2
    ry2 = y2 - h2


    if((x2 < x1 < rx2) and (ry2 < y1 < y2)) and ((x2 < rx1 < rx2) and (ry2 < ry1 < y2)):
        return(True)
    else:
        return(False)

def overlap(x1, y1, w1, h1, x2, y2, w2, h2):

    rx1 = x1 + w1
    ry1 = y1 - h1

    rx2 = x2 + w2
    ry2 = y2 - h2

    if((x2 <= x1 <= rx2) and (ry2 <= y1 <= y2) or ((x1 <= x2 <= rx1) and (ry1 <= y2 <= y1))):
        return(True)
  
    elif((x2 <= rx1 <= rx2) and (ry2 <= y1 <= y2)) or ((x1 <= rx2 <= rx1) and (ry1 <= y2 <= y1)):
        return(True)
   
    elif((x2 <= x1 <= rx2) and (ry2 <= ry1 <= y2)) or ((x1 <= x2 <= rx1) and (ry1 <= ry2 <= y1)):
        return(True)
  
    elif((x2 <= rx1 <= rx2) and (y2 <= ry1 <= ry2)) or ((x1 <= rx2 <= rx1) and (y1 <= ry2 <= ry1)):
        return(True)
        
    else:
        return(False)

def overlapRevised(x1, y1, w1, h1, x2, y2, w2, h2):

    rx1 = x1 + w1
    ry1 = y1 - h1

    rx2 = x2 + w2
    ry2 = y2 - h2

    if((x2 <= x1 <= rx2) and (ry2 <= y1 <= y2) or ((x1 <= x2 <= rx1) and (ry1 <= y2 <= y1))):
        return(True)
  
    elif((x2 <= rx1 <= rx2) and (ry2 <= y1 <= y2)) or ((x1 <= rx2 <= rx1) and (ry1 <= y2 <= y1)):
        return(True)
   
    elif((x2 <= x1 <= rx2) and (ry2 <= ry1 <= y2)) or ((x1 <= x2 <= rx1) and (ry1 <= ry2 <= y1)):
        return(True)
  
    elif((x2 <= rx1 <= rx2) and (y2 <= ry1 <= ry2)) or ((x1 <= rx2 <= rx1) and (y1 <= ry2 <= ry1)):
        return(True)
        
    else:
        return(False)


if __name__ == "__main__": # Only do the following if this file is called direfctly
    
   # year = int(input("Leap year: "))

    answer = overlapRevised(10,9,5,10, 4,1,6,4)

    print(answer)
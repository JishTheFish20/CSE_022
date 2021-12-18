import lab3

def testing_answers():
    assert  lab3.wages(34,18) == 612

def testingBloodDonationCompatibility():
    ################ A DONOR ###################
    assert lab3.canDonateBlood("A","A") == True
    assert lab3.canDonateBlood("A","AB") == True

    assert lab3.canDonateBlood("A","B") == False
    assert lab3.canDonateBlood("A","O") == False

    ################ B DONOR ###################
    assert lab3.canDonateBlood("B","B") == True
    assert lab3.canDonateBlood("B","AB") == True

    assert lab3.canDonateBlood("B","A") == False
    assert lab3.canDonateBlood("B","O") == False

    ################ AB DONOR ###################
    assert lab3.canDonateBlood("AB","AB") == True

    assert lab3.canDonateBlood("AB","A") == False
    assert lab3.canDonateBlood("AB","B") == False
    assert lab3.canDonateBlood("AB","O") == False


    ################ O DONOR ###################
    assert lab3.canDonateBlood("O","A") == True
    assert lab3.canDonateBlood("O","B") == True
    assert lab3.canDonateBlood("O","AB") == True
    assert lab3.canDonateBlood("O","O") == True

def testingLeapYear():
    assert lab3.leap(2020) == True
    assert lab3.leap(2000) == True
    assert lab3.leap(1900) == False
    assert lab3.leap(2019) == False

def testingDaysInMonth():
    assert lab3.daysInMonth(1,2021) == 31

def pointInRect():
    assert lab3.pointInRect(3, 3, 1, 5, 5, 3) == True
    assert lab3.pointInRect(1, 5, 1, 5, 5, 3) == True

def testOverLap():
    assert lab3.overlapRevised(1, 4, 5, 2, 0, 5, 8, 5) == True
    assert lab3.overlapRevised(10,9,5,10,4,1,6,4) == True    
    
    assert lab3.overlapRevised(4,9,7,2,2,3,4,1) == False     
    assert lab3.overlapRevised(1,10,8,10,3,2,10,10) == True     
    assert lab3.overlapRevised(10,7,2,9,8,1,4,7) == True     
    assert lab3.overlapRevised(0,10,10,10,2,8,4,4) == True     
    assert lab3.overlapRevised(3,10,7,4,2,1,5,2) == False     
    assert lab3.overlapRevised(-8,3,4,3,-7,1,2,3) == True     
    assert lab3.overlapRevised(1,1,1,1,1,1,1,1) == True     
    assert lab3.overlapRevised(-7,-2,9,6,-4,6,3,4) == False     
    assert lab3.overlapRevised(-6,6,4,6,-4,6,3,4) == True     
    assert lab3.overlapRevised(-6,6,4,6,-4,6,2,4) == True     
    assert lab3.overlapRevised(6,8,3,7,6,1,3,4) == True



import lab6

def testMax():
    assert lab6.maxInRange([1,2,3,4,5,6,7,8], 1, 3) == 4
    assert lab6.maxInRange([1,20,3,4,5,6,7,8], 1, 3) == 20

def testMin():
    assert lab6.minInRange([1,2,3,4,5,6,7,8], 1, 3) == 2
    assert lab6.minInRange([1,0,3,4,5,6,7,8], 1, 3) == 0
    assert lab6.minInRange([1,0,3,-1,5,6,7,8], 1, 3) == -1

def testCounter():
   assert lab6.elementCounter([1,3,1,4,1,5,1,6,1,7], 1) == 5

def testPosition():
   assert lab6.elementCounter([1,3,1,4,1,5,1,6,1,7], 1) == 5
   assert lab6.elementPos([1,3,1,4,1,5,1,6,1,7], 1) == [0, 2, 4, 6, 8]

def testRanges():
    assert lab6.ranges([1,2,3,4,5,6,7,8]) == [(1, 8)]
    assert lab6.ranges([0,1,2,4,5,7]) == [(0, 2), (4, 5), (7, 7)]
    assert lab6.ranges([0,2,3,4,6,8,9]) == [(0, 0), (2, 4), (6, 6), (8, 9)]
    assert lab6.ranges([]) == []

def testOccupy():
    assert lab6.occupySlot([0,1,1,0,0]) == [0, 1, 1, 0, 1]
    assert lab6.occupySlot([0,0,0,0,0]) == [1, 0, 1, 0, 1]
    assert lab6.occupySlot([0,1,0,0,0]) == [0, 1, 0, 1, 0]
    assert lab6.occupySlot([0,0,1,0,0]) == [1, 0, 1, 0, 1]

def testMisMatch():
    assert lab6.setMismatch([1,1]) == (1, 2)
    assert lab6.setMismatch([1,2,2,4]) == (2, 3)
    assert lab6.setMismatch([1,2,3,4,5,9,7,8,9,10]) == (9, 6)

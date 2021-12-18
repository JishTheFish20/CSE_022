import lab4

def testSimpleLock():
    assert lab4.simple_lock(1,1,1,1,1,2) == 1
    assert lab4.simple_lock(9,1,1,1,1,2) == 2
    assert lab4.simple_lock(9,5,1,1,9,2) == 6

def testComboLock():
    assert lab4.combo_lock(111, 232) == 4
    assert lab4.combo_lock(111, 112) == 1
    assert lab4.combo_lock(1151, 7122) == 7
    assert lab4.combo_lock(7929, 1384) == 13

def testPerfectNumbers():
    assert lab4.is_perfect(6) == True
    assert lab4.is_perfect(5) == False
    assert lab4.is_perfect(28) == True
    assert lab4.is_perfect(1) == False

def testNextPerfectNumbers():
    assert lab4.next_perfect(6) == 28
    assert lab4.next_perfect(28) == 496
    assert lab4.next_perfect(1) == 6

def testPrimeNumbers():
    assert lab4.is_prime(2) == True
    assert lab4.is_prime(5) == True
    assert lab4.is_prime(4) == False
    assert lab4.is_prime(9) == False
    assert lab4.is_prime(1) == False

def testNextPrimeNumbers():
    assert lab4.next_prime(2) == 3
    assert lab4.next_prime(5) == 7
    assert lab4.next_prime(4) == 5
    assert lab4.next_prime(37) == 41

def testPowers():
    assert lab4.is_power(8,2) == True
    assert lab4.is_power(9,2) == False
    assert lab4.is_power(1024, 2) == True

def testCoPrime():
    assert lab4.coprime(12,7) == True
    assert lab4.coprime(12, 8) == False

def testPhi():
    assert lab4.phi(17) == 16
    assert lab4.phi(16) == 8
def testSquareRoot():
    assert lab4.sqrt(3, 1, 0.0000001) == 1.7320508100147274
    assert lab4.sqrt(3, 1, 0.0000001) == 1.7320508100147274

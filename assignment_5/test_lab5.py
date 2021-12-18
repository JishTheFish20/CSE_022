import lab5

def testCountVowels():
    assert lab5.countVowels("Joshua") == 3
    assert lab5.countVowels("joshua") == 3
    

def testIsStable():
    assert lab5.isStable("Joshua") == False
    assert lab5.isStable("abba") == True
    assert lab5.isStable("abrba") == True
    assert lab5.isStable("ababa") == True
    assert lab5.isStable("abbaa") == False
    assert lab5.isStable("aroannillau") == True

def testHasDoubleLetters():
    assert lab5.hasDoubleLetters("abba") == True
    assert lab5.hasDoubleLetters("Hello") == True
    assert lab5.hasDoubleLetters("sheeesh") == True
    assert lab5.hasDoubleLetters("nope") == False

def testInterleave():
    assert lab5.interleave("111","222") == "121212"
    assert lab5.interleave("1234","56") == "152634"
    assert lab5.interleave("sheesh","bruh") == "sbhreuehsh"
    assert lab5.interleave("13579", "2468") == "123456789"
    assert lab5.interleave("02468", "13579") == "0123456789"
    assert lab5.interleave("hello", "hello") == "hheelllloo"
    assert lab5.interleave("hello", "") == "hello"
    assert lab5.interleave("", "hello") == "hello"

def testLCP():
    assert lab5.lcp("help","hello") == "hel"
    assert lab5.lcp("ApPle","OranGe") == ""
    assert lab5.lcp("flow", "flip") == "fl"
    assert lab5.lcp("fizz", "buzz") == ""

def testExtractLastName():
    assert lab5.extractLastName( "Steve Jobs","sjobs@ucmerced.edu") == "Jobs"
    assert lab5.extractLastName( "Miguel Carreira-Perpinan","mcarreira-perpinan@ucmerced.edu") == "Carreira-Perpinan"
    assert lab5.extractLastName("Franklin D. Roosevelt", "froosevelt@ucmerced.edu") == "Roosevelt"
    assert lab5.extractLastName("Jefferson Adam David Clark", "jdavidclark@ucmerced.edu") == "David Clark"


import lab7

def testHeading():
    assert lab7.heading("Some long title",20,4) == "---- Some lo... ----"
    assert lab7.heading("Heading Test") == "--------------------------------- Heading Test ---------------------------------"
    assert lab7.heading("") == "--------------------------------------------------------------------------------"
    assert lab7.heading("1") == "-------------------------------------- 1 ---------------------------------------"
    assert lab7.heading("10") == "-------------------------------------- 10 --------------------------------------"
    assert lab7.heading("101") == "------------------------------------- 101 --------------------------------------"
    assert lab7.heading("*" * 70) == "---- ********************************************************************** ----"
    assert lab7.heading("*" * 71) == "---- *******************************************************************... ----"
    assert lab7.heading("*" * 69) == "---- ********************************************************************* -----"

def testSummarizeFines():
    assert lab7.summarizeFines([['Jim', 100], ['Jeff', 75], ['Jane', 80], ['Juan', 110], ['Jim', 20]]) == [['Jim', 120], ['Jeff', 75], ['Jane', 80], ['Juan', 110]]

def testHighestDebtor():
    assert lab7.findHighestDebtor([['Jim', 100], ['Jeff', 75], ['Jane', 80], ['Juan', 110], ['Jim', 20]]) == "Jim"

def testOptimizeContainer():
    assert lab7.optimizeContainer(300 , [('Alice', 100), ('Bob', 233), ('Cecilia', 120), ('David', 130), ('Elizabeth', 95), ('Frank', 180)]) == ('Cecilia', 'Frank')

def testDropLowestGrades():
    assert lab7.dropLowestGrade("grades.txt") == [('Alice', [54, 61]), ('Bob', [54, 53]), ('Cecilia', [85, 91]), ('David', [64, 67]), ('Elizabeth', [87, 98]), ('Frank', [55, 43])]

def testAverageGrades():
    assert lab7.averageGrade([('Alice', [54, 61]), ('Bob', [54, 53]), ('Cecilia', [85, 91]), ('David', [64, 67]), ('Elizabeth', [87, 98]), ('Frank', [55, 43])]) == [('Alice', 57.5), ('Bob', 53.5), ('Cecilia', 88.0), ('David', 65.5), ('Elizabeth', 92.5), ('Frank', 49.0)]
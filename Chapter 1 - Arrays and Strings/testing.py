from interview_questions import *

def testing():
    # MAIN EXECUTION
    results = []
    tests = {
        "test1": ["isUnique1", testIsUnique1()],
        "test2": ["isUnique2", testIsUnique2()]
    }
    for test in tests:
        printTest(tests[test])

def printTest(test):
    # PRINTS TEST RESULTS
    name = test[0]
    (passed, failed) = test[1]
    print(name, "passed: ", passed, "failed: ", failed)

def testIsUnique1():
    # 1.1
    testsPassed = 0
    testsFailed = 0
    # TEST INPUT : EXPECTED RESULT
    tests = {
        'abcde': True,
        'abcda': False,
        'testing': False
    }
    for key in tests.keys():
        if(isUnique1(key) == tests[key]):
            testsPassed += 1
        else: 
            testsFailed += 1
    return testsPassed, testsFailed

def testIsUnique2():
    # 1.1
    testsPassed = 0
    testsFailed = 0
    # TEST INPUT : EXPECTED RESULT
    tests = {
        'abcde': True,
        'abcda': False,
        'testing': False,
        'boeing': True
    }
    for key in tests.keys():
        if(isUnique2(key) == tests[key]):
            testsPassed += 1
        else: 
            testsFailed += 1
    return testsPassed, testsFailed

testing()
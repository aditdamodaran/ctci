from interview_questions import *

def testing():
    # 1.1
    testsPassed = 0
    testsFailed = 0
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
    print("isUnique1: Tests Passed", testsPassed)
    print("isUnique1: Tests Failed",testsFailed)

testing()
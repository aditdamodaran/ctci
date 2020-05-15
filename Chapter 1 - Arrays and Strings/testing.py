from isUnique import *
from checkPermutation import *
from URLify import *

# ADD FUNCTIONS, ARGUMENTS, AND EXPECTED OUTPUT BELOW
# Format is a tuple (function, tests) where "tests" is a dictionary
testFunctions = [
    (
        isUnique1, {
            0: [('abcde'), True],
            1: [('abcda'), False],
            2: [('testing'), False]
        }
    ),
    (
        isUnique2, {
            0: [('abcde'), True],
            1: [('abcda'), False],
            2: [('testing'), False],
            3: [('boeing'), True]
        }
    ),
    (
        isPermutation1, {
            0: [('abcdee', 'cbeade'), True],
            1: [('apdsfinapsidfnaspoinfpaosinfopsin', 'aaaaddffffiiiiinnnnnooopppppsssss'), True]
        }
    ),
    (
        isPermutation2, {
            0: [('abcdee', 'cbeade'), True],
            1: [('apdsfinapsidfnaspoinfpaosinfopsin', 'aaaaddffffiiiiinnnnnooopppppsssss'), True]
        }
    ),
    (
        isPermutation3, {
            0: [('abcdee', 'cbeade'), True],
            1: [('apdsfinapsidfnaspoinfpaosinfopsin', 'aaaaddffffiiiiinnnnnooopppppsssss'), True],
            2: [('nascar', 'racsna'), True],
            3: [('hamburger', 'hamburgular'), False]    
        }
    ),
    (
        URLify1, {
            0: [('Mr John Smith    ', 13), 'Mr%20John%20Smith'],
            1: [('   ', 1), '%20'],
            2: [('      ', 2), '%20%20'],
            3: [(' This tests another case        ', 24), '%20This%20tests%20another%20case'],
            4: [(' this  is  a different  kind   of case                                 ', 41),'%20this%20%20is%20%20a%20different%20%20kind%20%20%20of%20case%20%20%20']
        }
    )
]

def printTest(test):
    # PRINTS TEST RESULTS
    name = test[0]
    (passed, failed) = test[1]
    print(name, "passed: ", passed, "failed: ", failed)

def testingFramework(function, args, expected):
    # Checks if unit test passed
    if(function(args) == expected):
        return True
    else:
        return False

def testOne(fxn):
    for i, testFunction in enumerate(testFunctions):
        if (testFunction[0] == fxn):
            testsPassed = 0
            testsFailed = 0
            function = testFunction[0]
            tests = testFunction[1]
            for test in tests.keys():
                args = tests[test][0]
                expected = tests[test][1]
                result = testingFramework(function, args, expected)
                if (result):
                    testsPassed += 1
                else: 
                    testsFailed += 1      
            printTest([str(function.__name__), (testsPassed, testsFailed)])


def testAll():
    for i, testFunction in enumerate(testFunctions):
        testsPassed = 0
        testsFailed = 0
        function = testFunction[0]
        tests = testFunction[1]
        for test in tests.keys():
            args = tests[test][0]
            expected = tests[test][1]
            result = testingFramework(function, args, expected)
            if (result):
                testsPassed += 1
            else: 
                testsFailed += 1      
        printTest([str(function.__name__), (testsPassed, testsFailed)])

def main():
    print("\n" + "-------------------------------------------------")
    # testAll()
    testOne(URLify1)
    print("-------------------------------------------------" + "\n")

main()
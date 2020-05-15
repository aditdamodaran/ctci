from interview_questions import *

# ADD FUNCTIONS, ARGUMENTS, AND EXPECTED OUTPUT BELOW
# Format is a tuple (function, tests) where "tests" is a dictionary
testFunctions = [
    (
        isUnique1,{
            0: [('abcde'), True],
            1: [('abcda'), False],
            2: [('testing'), False]
        }
    ),
    (
        isUnique2,{
            0: [('abcde'), True],
            1: [('abcda'), False],
            2: [('testing'), False],
            3: [('boeing'), True]
        }
    ),
    (
        isPermutation1,{
            0: [('abcdee', 'cbeade'), True],
            1: [('apdsfinapsidfnaspoinfpaosinfopsin', 'aaaaddffffiiiiinnnnnooopppppsssss'), True]
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

def testing():
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
    testing()
    print("-------------------------------------------------" + "\n")

main()
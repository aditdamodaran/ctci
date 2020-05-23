from isUnique import *
from checkPermutation import *
from URLify import *
from checkPalindromePermutation import *
from oneAway import *
from stringCompression import *
from stringRotation import *

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
    ),
    (
        checkPalindrome1, {
            0: [('Tact Coa'), True],
            1: [('Hydeydh'), True],
            2: [('Haisnfpaosin'), False],
            3: [('a nasa at santa'), True],
            4: [('racecars'), False],
            5: [('racecar'), True],
            6: [('daaaaadeeee'), True],
            7: [('dad'), True],
            8: [('dated'), False]
        }
    ), 
    (
        oneAway1, {
            0: [('pale','ple'), True],
            1: [('pales','pale'), True],
            2: [('pale','bale'), True],
            3: [('pale','bake'), False],
            4: [('hello','hells'), True],
            5: [('hello','ello'), True],
            6: [('hello','henlo'), True],
            7: [('hello','ellis'), False],
            8: [('hello','ells'), False],
            9: [('a','b'), True],
            10: [('','d'), True],
            11: [('d','de'), True],
            12: [('pale','pse'), False],
            13: [('pkle','pable'), False],
            14: [('pal','palks'), False],
            15: [('palks','pal'), False],
            16: [('hello', 'ollehs'), False]
        }
    ),
    (
        stringCompression1, {
            0: [('aabcccccaaa'), 'a2b1c5a3'],
            1: [('aa'), 'aa'],
            2: [('cCdD'), 'cCdD'],
            3: [('aaFFeRiJKllllllllmnooooooooo'), 'a2F2e1R1i1J1K1l8m1n1o9'],
            4: [('aaa'), 'a3']
        }
    ),
    (
        stringRotation1, {
            0: [('waterbottle','erbottlewat'), True],
            1: [('foo','bar'), False],
            2: [('foo','foofoo'), False]
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
    result = function(args)
    if(result == expected):
        # UNCOMMENT FOR DEBUGGING
        # print("PASSED TEST: " + str(function.__name__) + " passed. with argument(s): " + str(args) + "\n \t\t Expected: " + str(expected) + ". Actual: " + str(result))
        return True
    else:
        print("FAILED TEST: " + str(function.__name__) + " failed. with argument(s): " + str(args) + "\n \t\t Expected: " + str(expected) + ". Actual: " + str(result))
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
    testAll()
    # testOne(checkPalindrome1)
    print("-------------------------------------------------" + "\n")

main()
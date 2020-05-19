"""
1.6 String Compression:
Given a string 'aabcccccaaa', convert it to 'a2b1c5a3'. If the compressed string is not smaller than
the original string, return the original string. Assume only uppercase and lowercase letters.
"""
# Implementation 1 
# Description: Recursive Implementation using Helper Function and Creating a New String along the way
# Runtime: O(N) -- we only iterate through the string once
# Space Complexity: O(N) (a new string of size 'N')
def stringCompressionHelper(oldString,string,newString):
    # Exit when there is only one unique character left to go 
    exitCondition = False
    if len(set(string)) == 1:
        exitCondition = True

    # Iterate through all repeated instances of the same character
    check = string[0]
    checkCounter = 0
    i = 0
    while (string[i]==check and i<len(string)-1): 
        i+=1
        checkCounter+=1
    
    # Add one more if we're at the end
    if(exitCondition):
        checkCounter+=1
    
    # Add the character and its count to the newString
    newString+=check
    newString+=str(checkCounter)

    # If we're exiting, quickly check that we have arrived at a shorter string
    # or return the original string
    if (exitCondition):
        if (len(oldString) > len(newString)):
            return newString
        else:
            return oldString
    
    # If we're not exiting, recursion is used to continue down the string
    return stringCompressionHelper(oldString, string[i:], newString)


def stringCompression1(args):
    string = args
    return stringCompressionHelper(string,string, "")
"""
1.3 URLify: 
Write a method to replce all spaces in a string with '%20'. 
String has sufficient space @ end to hold additional characters (no memory alloc required).
i.e. "Mr. John Smith    " would have 4 spaces at the end.
You are given the "true" length of the original string (i.e. 13 for the above example).  
"""
# Implementation 1 
# Description: Find spaces, and then reassign string mathematically starting from end
# Runtime: O(N)
# Space Complexity: O(N)
def URLify1(args):
    # Unpack and Convert to Array of Characters
    string, length = args
    string = list(string)

    # Keep track of where spaces are, and how many
    countSpaces = 0
    spaceIndex = []
    for i in range(0, len(string) - 1):
        if (string[i] == " " and i < (length)):
            countSpaces += 1
            spaceIndex.append(i)

    # Starting from the string's end, 
    # shift characters as calculated

    shift = countSpaces*2
    idxsRev = list(range(0,length))[::-1]

    for idx in idxsRev:
        if (idx not in spaceIndex):
            # encountering non-space characters
            string[idx+shift] = string[idx]
        else:
            # encountering an index with a space
            shift -= 2
            string[idx+shift+2] = "0"
            string[idx+shift+1] = "2"
            string[idx+shift] = "%"

    return "".join(string)
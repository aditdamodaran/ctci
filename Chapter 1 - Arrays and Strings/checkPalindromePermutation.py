"""
1.3 Check Palindrome Permutation:
Given a string, check if it is a permutation of a palindrome.
"""
# Implementation 1 (Naive)
# Description: If odd in length, check for pairs for all letters (except 1)
# ... If even, check for pairs for all letters
# Runtime: O(N)
# Space Complexity: O(N)
def checkPalindrome1(args):
    # Unpack and Convert to Array of Characters
    string = args
    # Ignore spaces and capitalization
    string = "".join(string.lower().split())
    string = list(string)

    
    chars = {}
    # Create a Dictionary of characters
    for char in string:
        if char in chars.keys():
            chars[char] += 1
        else:
            chars[char] = 1
    if (len(string)%2 == 0):
        # If the total # of chars in the string is even
        # Return true unless we find an odd # of a character
        for char in chars.keys():
            if (chars[char]%2 != 0):
                return False
            else:
                continue
        return True
    else:
        # If the total # of chars in the string is odd
        # Return true only if there is NOT an odd number of multiple chars
        numOdd = 0
        for char in chars.keys():
            if (chars[char]%2 != 0):
                numOdd += 1
        if (numOdd != 1):
            return False
        return True

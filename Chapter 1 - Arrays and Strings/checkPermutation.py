"""
1.2 Check Permutation: 
Given two strings,write a method to decide if 
one is a permutation of the other.
"""
# Implementation 1 (Naive)
# Description: Use Hashtables to Compare
# Runtime: If length of STR1 is A, and length of STR2 is B, and # of Unique CHARS is M: O(MAB)
# Space Complexity: O(M)
def isPermutation1(args):
    """Uses Hash Table to check character frequencies"""
    str1, str2 = args
    
    # Same Length is the quickest check
    if len(str1) != len(str2):
        return False

    chars1 = {}
    for char in str1:
        if (char in chars1.keys()):
            chars1[char] += 1
        else:
            chars1[char] = 1
    for char in str2:
        if (char in chars1.keys()):
            chars1[char] -= 1
        else:
            return False
    if (sum(chars1.values()) == 0):
        return True
    else:
        return False

# Implementation 2 (Naive)
# Description: Sort Strings, then Compare
# Runtime: O(N^2) where N is the length of the strings
# Space Complexity: O(1)
def bubbleSort(arr): 
    n = len(arr) 
    # Traverse through all array elements 
    for i in range(n-1): 
        # Last i elements are already in place 
        for j in range(0, n-i-1): 
            # traverse the array from 0 to n-i-1 
            # Swap if the element found is greater 
            # than the next element 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j]

def isPermutation2(args):
    """Sort Strings, then Compare"""
    str1, str2 = args

    # Same Length is the quickest check
    if len(str1) != len(str2):
        return False

    str1 = list(str1)
    str2 = list(str2)
    bubbleSort(str1)
    bubbleSort(str2)
    ''.join(str1)
    ''.join(str2)
    return True if str1 == str2 else False
    

# Implementation 3 
# Description: Use an array (length n for n unique characters) with zeroes, and increment for each
# ...char in str1, then decrement for each char in str2. If SUM is 0, then they are permutations.
# Assumption: ASCII Chars Only (128 Max)
# Runtime: O(2N)
# Space Complexity: O(N)

def isPermutation3(args):
    """Check with array"""
    str1, str2 = args

    # Same Length is the quickest check
    if len(str1) != len(str2):
        return False

    arr = [0 for _ in range(128)]
    for char in str1:
        val = ord(char)
        arr[val] += 1
    for char in str2:
        val = ord(char)
        arr[val] -= 1

        # Early Exit Case
        if (sum(arr) < 0):
            return False

    return True if (sum(arr) == 0) else False







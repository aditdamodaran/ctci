"""
1.1 Is Unique:
Implement an algorithm to determine if a string has all unique
characters. What if you cannot use additional data structures?
"""

# Implementation 1
# Runtime: O(N^2)
# Space Complexity: O(N) (maxes at # of unique chars)
def isUnique1(string):
    """ Use a hash table / dictionary to check for unique
    characters """
    chars = {}
    for char in string:
        if (char in chars.keys()):
            return False
        else:
            chars[char] = 1
    return True

# Implementation 2
# Runtime: O(N)
# Space Complexity: O(1) (maxes at 26 bits)
def isUnique2(string):
    """Use 26 bits of an INT32 to check for duplicates --
    makes the assumption of using 26 letters of the alphabet
    and also case-insensitive"""
    checker = 0
    for char in string:
        val = ord(char.lower()) - 97
        if (checker & (1 << val)) > 0: 
            # print("FALSE",'{:026b}'.format(1 << val))
            # print("FALSE",'{:0266b}'.format(checker))
            return False
        checker |= (1 << val)
        # print("TRUE",'{:026b}'.format(1 << val))
        # print("TRUE",'{:026b}'.format(checker))
    return True

"""
1.2 Check Permutation: 
Given two strings,write a method to decide if 
one is a permutation of the other.
"""
# Implementation 1
# Runtime: If length of STR1 is A, and length of STR2 is B, and # of Unique CHARS is M: O(MAB)
# Space Complexity: O(M)
def isPermutation1(str1, str2):
    """Uses Hash Table to check character frequencies"""
    chars1 = {}
    for char in str1:
        if (char in chars1.keys()):
            chars1[char] += 1
        else:
            chars1[char] = 1
    print(chars1)
    for char in str2:
        if (char in chars1.keys()):
            chars1[char] -= 1
        else:
            return False
    print(chars1)
    if (sum(chars1.values()) == 0):
        return True
    else:
        return False

# print(isPermutation1('abcdee', 'cbeade'))
# print(isPermutation1('apdsfinapsidfnaspoinfpaosinfopsin', 'aaaaddffffiiiiinnnnnooopppppsssss'))







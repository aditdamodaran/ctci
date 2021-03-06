"""
1.1 Is Unique:
Implement an algorithm to determine if a string has all unique
characters. What if you cannot use additional data structures?
"""

# Implementation 1 (Naive)
# Description: Use Hashtable ot Check for Unique Characters
# Runtime: O(N^2)
# Space Complexity: O(N) (maxes at # of unique chars)
def isUnique1(args):
    string = args
    """ Use a hash table / dictionary to check for unique
    characters """
    chars = {}
    for char in string:
        if (char in chars.keys()):
            return False
        else:
            chars[char] = 1
    return True

# Implementation 2 (Bit Manip.)
# Description: Use a bitmap (length n for n unique characters) with 0 or 1 values for unique chars.
# ...if a character encounters a value already set to 1, the string is not unique.
# Runtime: O(N)
# Space Complexity: O(1) (maxes at 26 bits)
def isUnique2(args):
    string = args
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

"""
1.9 String Rotation:
Given two strings, check if str2 is a rotation str1 using only one call to an "isSubstring" method, which
returns a boolean for whether strX is a substring of strY
"""
# Helper (Given)
def isSubstring(args):
    str1, str2 = args
    return True if str2 in str1 else False

# Implementation 1 
# Description: This one is less about finding an optimal solution, and more about the logic puzzle. 
# The book's solution gives a great explanation.
# Runtime: O(N) (this is the time complexity of the 'in' keyword in isSubstring for a string)
# Space Complexity: O(2N) -- double whatever the length of the given string arguments are.
def stringRotation1(args):
    str1, str2 = args
    xyxy = str1 + str1
    return isSubstring((xyxy, str2)) and len(str1) == len(str2)




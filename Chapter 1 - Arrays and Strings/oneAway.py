"""
1.5 One Away:
Given two strings, check if str1 is "one edit" (insert, remove, or replace a char) or less away from str2 
"""
# Implementation 1 
# Description: Iterate through the short string, and try to insert or replace along the way
# Runtime: O(N) (length of short string)
# Space Complexity: O(1)
def oneAway1(args):
    str1, str2 = args

    ### VALIDATORS ###
    if (str1 == str2):
        return True
    # Must be within at least 1 char of each other
    if abs(len(str1) - len(str2)) > 1:
        return False
    
    # Determine which string is shorter. 
    # Short String = ss
    # Long String = ls
    if len(str2) - len(str1) > 0 :
        ss = list(str1)
        ls = list(str2)
    elif len(str2) - len(str1) < 0:
        ss = list(str2)
        ls = list(str1)
    else:
        ss = list(str1)
        ls = list(str2)
    
    # Edge case (add a single char to empty short string)
    if (len(ss) == 0):
        ss.append(ls[0])
        if (ss == ls):
            return True
        else:
            return False

    for i in range(0, len(ss)):
        # Find where the first difference occurs
        if (ss[i] != ls[i]):
            missingChar = ls[i]

            # Try an Insert
            ss.insert(i, missingChar)
            if (ss == ls):
                return True
            else:
                ss.pop(i)
            
            # Try a Replace
            temp = ss[i]
            ss[i] = missingChar
            if (ss == ls):
                return True
            else:
                ss[i] = temp
            
            # Check that they've been the same up till now
            if (ss[:i] != ls[:i]):
                return False

    # If so, try an Insert at the End of the Short String
    # If this doesn't work, we've exhausted all options
    ss.append(ls[i+1]) 
    return True if (ss == ls) else False



"""
1.4 One Away:
Given two strings, check if str1 is "one edit" (insert, remove, or replace a char) or less away from str2 
"""


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


























# Implementation 1
# Description: Assuming we are only using ASCII characters, use a similar solution to "isUnique", but 
# ... compare the two strings tabulations to one another. If Edit Distance <2, we're set.
# Runtime: O(AB) where A is len(str1) and where B is len(str2)
# Space Complexity: O(1) 
# def bubbleSort(arr): 
#     n = len(arr) 
#     # Traverse through all array elements 
#     for i in range(n-1): 
#         # Last i elements are already in place 
#         for j in range(0, n-i-1): 
#             # traverse the array from 0 to n-i-1 
#             # Swap if the element found is greater 
#             # than the next element 
#             if arr[j] > arr[j+1] : 
#                 arr[j], arr[j+1] = arr[j+1], arr[j]

# def oneInsertorRemovalAway(str1, str2):
#     # "helo" "hello"
#     # "hello" "helolo"
#     # Where len(str1) < len(str2)
#     str1 = list(str1)
#     str2 = list(str2)
#     for i in range(0,len(str1)):
#         if(str1[i] == str2[i]):
#             continue
#         else:
#             break
    
    # try an insert
    # print(str1[i:], str2[i:])
    # try:
    #     str1[i] = str2[i]
    #     str1[i+1:] = str2[i+1:]
    #     if (str1 == str2):
    #         return True
    # except:
    #     return False
    # print(str1)
    # str1[i] = str2[i]
    # print(i, str1[i], str2[i])

# oneInsertorRemovalAway('helo', 'hello')
# print(oneInsertorRemovalAway('cardgame', 'cargames'))
# oneInsertorRemovalAway('hello', 'helolo')




# def oneAway1(args):
#     str1, str2 = args

#     if (str1 == str2):
#         return True
    
#     # Must be within at least 1 char of each other
#     if abs(len(str1) - len(str2)) > 1:
#         return False
    
    
    
    # create lists of zeroes 128 in length (to fit all ASCIIs)
    # tab1,tab2 = [0 for _ in range(128)],[0 for _ in range(128)]
    # result = [0 for _ in range(128)]

    # cumulative total of how many times each character appears
    # for char in str1:
    #     val = ord(char)
    #     tab1[val] += 1
    # for char in str2:
    #     val = ord(char)
    #     tab2[val] += 1
    
    # print(tab1)
    # print(tab2)

    # Compare the two strings in edit distance
    # for i in range(0,len(tab1)):
    #     result[i] = abs(tab1[i] - tab2[i])
    # return True if (sum(result) <= 2) else False

    # Commenting out a Visualization
    # tab1 = ''.join(map(str, tab1))
    # tab2 = ''.join(map(str, tab2))
    # result = ''.join(map(str, result))
    # print(tab1)
    # print(tab2)
    # print(result)

# oneAway1(('hello','ollehs'))


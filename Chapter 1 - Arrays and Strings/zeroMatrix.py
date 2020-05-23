"""
1.8 Zero Matrix
IF given an MxN matrix, if any cell is "0", we set the entire row and column = 0
"""
# HELPER FUNCTIONS FOR EASE OF TESTING AND VISUALIZATION
def printMatrix(m):
    print('\n')
    for row in m:
        print(row)
    print('\n')

def createMatrix(M,N):
    matrix = []
    # Used for testing
    for i in range(0,M):
        row = []
        for j in range(N*i,(N*i)+N):
            # add leading zeroes to make printing prettier when N>3
            idx = str(j+1).zfill(len(str(N*N)))
            row.append(idx)
        matrix.append(row)
    return matrix

# Implementation 1 
# Description: First set entire column to zero, but record rows where a zero was found. Then set row = 0.
# Runtime: O(MN) to O(M^2N) -- we iterate through the whole matrix, then just the rows where we found zeroes
# Space Complexity: O(MN) in worst case -- Just the dictionary where we store zero's indices 

# This algorithm could be improved by immediately nullifying an entire row or column as soon
# as a zero is found. This is basically what the official solution does. It keeps track of 
# x and y coordinates for the zeroes in a list (or bit vector), and then nullifies accordingly.
def zeroMatrix1(matrix):
    M = len(matrix)
    save = {}

    # ITERATE THROUGH EVERY ROW
    for x, row in enumerate(matrix):
        # AND THEN EVERY CELL IN EVERY ROW
        for i, cell in enumerate(row):
            # IF WE FIND A ZERO CELL
            cell = int(cell)
            if (cell == 0 and i not in save.keys()):
                # SAVE ITS ROW AND COLUMN TO A DICT
                save[i] = x
                N = len(row)
                zero = str('0').zfill(len(str(N*N)))
                # SET THE WHOLE COLUMN TO ZERO
                while(x != 0):
                    x-=1
                    matrix[x][i] = zero
                while (x < M-1):
                    x+=1
                    matrix[x][i] = zero

    # FOR ANY ROW WHERE WE ENCOUNTERED A ZERO EARLIER
    for row in save.keys():
        for j, cell in enumerate(matrix[save[row]]):
            # SET THE WHOLE ROW TO ZERO
            while(j != 0):
                j-=1
                matrix[save[row]][j] = zero
            while(i < N-1):
                i+=1
                matrix[save[row]][i] = zero


testMatrix1 = createMatrix(5,6)
testMatrix1[4][5] = "00"
testMatrix1[2][1] = "00"
printMatrix(testMatrix1)
zeroMatrix1(testMatrix1)
printMatrix(testMatrix1)

testMatrix2 = createMatrix(2,3)
testMatrix2[0][1] = "0"
testMatrix2[1][2] = "0"
printMatrix(testMatrix2)
zeroMatrix1(testMatrix2)
printMatrix(testMatrix2)

testMatrix3 = createMatrix(10,12)
testMatrix3[4][8] = "000"
testMatrix3[3][9] = "000"
testMatrix3[9][10] = "000"
printMatrix(testMatrix3)
zeroMatrix1(testMatrix3)
printMatrix(testMatrix3)

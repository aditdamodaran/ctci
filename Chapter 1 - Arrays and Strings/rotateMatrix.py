from math import floor

"""
1.7 Rotate Matrix:
Given a NxN matrix, "rotate it" 90 degrees in place.
"""
# HELPER FUNCTIONS FOR EASE OF TESTING AND VISUALIZATION
def printMatrix(m):
    print('\n')
    for row in m:
        print(row)
    print('\n')

def createMatrix(N):
    matrix = []
    # Used for testing
    for i in range(0,N):
        row = []
        for j in range(N*i,(N*i)+N):
            # add leading zeroes to make printing prettier when N>3
            idx = str(j+1).zfill(len(str(N*N)))
            row.append(idx)
        matrix.append(row)
    return matrix

# Implementation 1 (InPlace)
# Description: Explanation Link: https://www.geeksforgeeks.org/inplace-rotate-square-matrix-by-90-degrees/
# Runtime: O(N^2)
# Space Complexity: O(1)
def rotateMatrix1(matrix):
    # Calculate # of Cycles = floored distance from (0,0) to center of matrix along diagonal
    # (a 3x3 has one cycle, a 2x2 has one cycle, but a 4x4 and 5x5 have two)
    n = len(matrix)
    cycles = floor(n/2)
    printMatrix(matrix)
    for c in range(0, cycles):
        # 4 rotations each cycle for n-1 cells
        for i in range(c, n-c-1):
            # Convert negative indexes to normal indexes by adding N
            
            # Save Top 
            top = matrix[c][i] 

            """
            Keeping these for reference
            left = matrix[n-1-i][c]
            bottom = matrix[n-1-c][n-1-i]
            right = matrix[i][n-1-c] 
            """

            # Swap Left + Top
            matrix[c][i] = matrix[n-1-i][c]

            # Swap Bottom + Left
            matrix[n-1-i][c] = matrix[n-1-c][n-1-i]

            # Swap Right + Bottom
            matrix[n-1-c][n-1-i] = matrix[i][n-1-c]

            # Swap Top + Right
            matrix[i][n-1-c] = top
    
    return matrix

fiveByFive = createMatrix(5)
printMatrix(rotateMatrix1(fiveByFive))

tenByTen= createMatrix(10)
printMatrix(rotateMatrix1(tenByTen))

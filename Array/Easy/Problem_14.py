# Given a square matrix mat, return the sum of the matrix diagonals.
# Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.

# Example 1:
# Input: mat = [[1,2,3],
#               [4,5,6],
#               [7,8,9]]
# Output: 25
# Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
# Notice that element mat[1][1] = 5 is counted only once.

# SOLUTION

def diagonalSum(mat):
    n = len(mat[0])
    diagSum = [0,0]
    odd = n%2
    
    for i in range(1):
        for j in range(n):
            if odd and j == (n//2):
                diagSum[0] += mat[j][j]
            else:
                diagSum[0] += mat[j][j]
                diagSum[1] += mat[j][n-1-j]

    return diagSum[0] + diagSum[1]      

diagonalSum([[1,2,3], [4,5,6], [7,8,9]])
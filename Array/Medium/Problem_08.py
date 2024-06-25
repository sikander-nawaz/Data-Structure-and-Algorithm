# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
# You must do it in place.
 
# Example 1:
# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]

# SOLUTION:

def setZeroes(matrix):
     row = set()
     col = set()

     for i in range(len(matrix)):
          for j in range(len(matrix[i])):
               if matrix[i][j] == 0:
                    row.add(i)
                    col.add(j)
     for i in range(len(matrix)):
          for j in range(len(matrix[i])):
               if i in row or j in col:
                    matrix[i][j] = 0
     return matrix
        
setZeroes([[1,1,1],[1,0,1],[1,1,1]])
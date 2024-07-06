# Given a 2D integer array matrix, return the transpose of matrix.
# The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices. 

# Example 1:
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[1,4,7],[2,5,8],[3,6,9]]

# SOLUTION:

def transpose(matrix):
     row = len(matrix)              
     colum = len(matrix[0])       

     result = [[0] * row for _ in range(colum)] 
        
     for i in range(colum):                    
          for j in range(row):
               result[i][j] = matrix[j][i]

     return result

matrix = [[1,2,3],[4,5,6],[7,8,9]]
transpose(matrix)
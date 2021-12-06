# https://leetcode.com/problems/spiral-matrix/

from typing import List


'''
Logic :
Repeat till matrix is consumed
{
step 1) Extract First Row & append all elements to ans list
step 2) Reverse Each Row
step 3) Transpose of resulted matrix
}

'''

def spiralOrder(matrix: List[List[int]]) -> List[int]:
    '''
        traverse matrix in spiral order clock-wise
    '''
    spiral_traverse = []
    while matrix:
        first_row = matrix.pop(0)
        spiral_traverse.extend(first_row)
        matrix = list(zip(*map(reversed, matrix)))
    return spiral_traverse


def reverseSpiralOrder(matrix: List[List[int]]) -> List[int]:
    '''
        traverse matrix in spiral order anti-clock-wise
        Steps :- 1) Transpose of a given matrix
                 2) Do a Spiral Order Traverse
    '''
    *matrix, = zip(*matrix)
    anti_spiral_traverse = spiralOrder(matrix)
    return anti_spiral_traverse


matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
#ans1 = spiralOrder(matrix)
ans2 = reverseSpiralOrder(matrix)

#print(ans1)
print(ans2)

def spiralOrder3(matrix: List[List[int]]) -> List[int]:
    m, n = len(matrix), len(matrix[0]) # Initial possible number of steps
    direction = 1 # Start off going right
    i, j = 0, -1
    output = []
    while m*n > 0:
        for _ in range(n): # move horizontally
            j += direction
            output.append(matrix[i][j])
        m-= 1
        for _ in range(m): # move vertically
            i += direction
            output.append(matrix[i][j])
        n-=1
        direction *= -1 # flip direction
    return output
    
            

class Solution(object):
    def rotate(self, matrix):
        rows=len(matrix)
        cols=len(matrix[0])
        result=[[0]*rows for _ in range(cols)]
        for i in range(rows):
            for j in range(cols):
                result[j][rows-i-1]=matrix[i][j]
        matrix[:]=result
        

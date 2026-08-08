class Solution(object):
    def spiralOrder(self, matrix):
        l=[]
        top=0
        right=len(matrix[0])-1
        bottom=len(matrix)-1
        left=0
        while top<=bottom and left<=right:
            for i in range(left,right+1):
                l.append(matrix[top][i])
            top+=1
            for j in range(top,bottom+1):
                l.append(matrix[j][right])
            right-=1
            if top<=bottom:
                for k in range(right,left-1,-1):
                    l.append(matrix[bottom][k])
                bottom-=1
            if left<=right:
                for m in range(bottom,top-1,-1):
                    l.append(matrix[m][left])
                left+=1
        return l

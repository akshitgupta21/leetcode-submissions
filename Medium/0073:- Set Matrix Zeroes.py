class Solution(object):
    def setZeroes(self, nums):
        rows=len(nums)
        column=len(nums[0])
        r_trace=[0 for _ in range(rows)]
        c_trace=[0 for _ in range(column)]
        for i in range(rows):
            for j in range(column):
                if nums[i][j]==0:
                    r_trace[i]=-1
                    c_trace[j]=-1

        for l in range(rows):
            for m in range(column):
                if r_trace[l]==-1 or c_trace[m]==-1:
                    nums[l][m]=0

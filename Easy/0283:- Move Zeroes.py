class Solution(object):
    def moveZeroes(self, nums):
        e=nums.count(0)
        for i in range(e):
            nums.remove(0)
            nums.append(0)

class Solution(object):
    def sortColors(self, nums):
        a=nums.count(0)
        b=nums.count(1)
        c=nums.count(2)
        del nums[:]
        nums[:]=[0]*a + [1]*b +[2]*c

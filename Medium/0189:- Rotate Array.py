class Solution(object):
    def rotate(self, nums, k):
        n=len(nums)
        k%=n
        nums[:]=list(nums[n-k:n])+list(nums[0:n-k])

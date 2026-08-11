class Solution(object):
    def searchRange(self, nums, target):
        l=0
        h=len(nums)-1
        lb=-1
        ub=len(nums)
        low=0
        high=len(nums)-1
        while low<=high:
            mid=(high+low)//2
            if nums[mid]>target:
               ub=mid
               high=mid-1
            else:
                low=mid+1
        while l<=h:
            m=(l+h)//2
            if nums[m]>=target:
                lb=m
                h=m-1
            else:
                l=m+1
        if lb==-1 or ub-1<lb:
            return [-1,-1]
        return [lb,ub-1]

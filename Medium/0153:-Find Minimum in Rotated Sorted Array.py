class Solution(object):
    def findMin(self, nums):
        low=0
        high=len(nums)-1
        l=5000
        while low<=high:
            mid=(low+high)//2
            m=min(nums[low],nums[high],nums[mid])
            if l>=m:
                l=m
            if nums[mid]<=nums[high]:
                if nums[mid]<=l<=nums[high]:
                    l=nums[mid]
                    high=mid-1
                else:
                    high=mid-1
            else:
                if nums[low]<=l<=nums[mid]:
                    l=nums[low]
                    low=mid+1
                else:
                    low=mid+1
        return l

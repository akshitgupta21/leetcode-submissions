class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i=0
        while i!=len(nums):
            contain=target-nums[i]
            for j in range(i):
                if nums[j]==contain:
                    return [j,i]
            i+=1

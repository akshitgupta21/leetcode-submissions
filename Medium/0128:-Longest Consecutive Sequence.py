class Solution(object):
    def longestConsecutive(self, nums):
        s=list(set(nums))
        s.sort()
        count=0
        last_smaller=float("-inf")
        longest=0
        for i in range(len(s)):
            if last_smaller==s[i]-1:
                last_smaller=s[i]
                count+=1
            elif s[i]-1!=last_smaller:
                count=1
                last_smaller=s[i]
            longest=max(longest,count)
        return longest

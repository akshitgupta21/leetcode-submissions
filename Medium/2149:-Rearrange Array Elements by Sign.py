class Solution(object):
    def rearrangeArray(self, nums):
        l=[]
        p=[]
        n=[]
        for i in nums:
            if i<0:
                n.append(i)
            else:
                p.append(i)
        for j in range(len(nums)/2):
            l.append(p[j])
            l.append(n[j])
        return l

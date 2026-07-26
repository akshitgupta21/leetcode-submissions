class Solution(object):
    def topKFrequent(self, nums, k):
        l=list(set(nums)) 
        d=[] 
        for i in l:
            b=nums.count(i) 
            d.append(b)
        s=[] 
        for i in range(k):
            f=max(d) 
            g=d.index(f) 
            s.append(l[g]) 
            d.remove(f) 
            l.remove(l[g])

        return s

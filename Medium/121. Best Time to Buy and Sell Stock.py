class Solution(object):
    def maxProfit(self, prices):
        m=float("inf")
        x=0
        for i in range(len(prices)):
            if prices[i]<m:
                m=prices[i]
            if prices[i]-m>x:
                x=prices[i]-m
        return x

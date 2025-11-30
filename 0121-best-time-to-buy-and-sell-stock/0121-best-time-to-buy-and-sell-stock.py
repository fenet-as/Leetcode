class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p = 0

        mn = prices[0]
        for e in prices:
            if e < mn:
                mn = e
            p = max(p,e-mn)
        return p
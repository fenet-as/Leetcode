class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mn = float('inf')
        mx = 0


        for e in prices:
            mn = min(mn,e)
            mx = max(mx,e - mn)
        return mx

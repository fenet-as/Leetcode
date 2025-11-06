class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        mn = float('inf')
        mxp = 0
        for e in prices:
            mn = min(e,mn)
            mxp = max(mxp,e-mn)
        

        return mxp


     
       
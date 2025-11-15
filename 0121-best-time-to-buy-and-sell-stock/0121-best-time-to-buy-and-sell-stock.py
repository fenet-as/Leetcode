class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        keep mn while going
        keep cn - mn while going
        '''
        mn = float('inf')
        mp = 0
        for e in prices:
            mn = min(mn,e)
            cp = e - mn
            mp = max(mp,cp)
        return mp

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()

        i = 0
        j = len(piles)-2

        ct = 0
        while i < j:
            ct += piles[j]
            j -= 2
            i += 1
        return ct

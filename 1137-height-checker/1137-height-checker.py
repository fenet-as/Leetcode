class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        ex = heights.copy()

        ex.sort()

        ct = 0
        for i in range(len(heights)):
            if ex[i] != heights[i]:
                ct += 1
        return ct
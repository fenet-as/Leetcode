class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        exp = heights.copy()
        exp.sort()

        ct = 0
        for i in range(len(heights)):
            if exp[i] != heights[i]:
                ct += 1
        return ct
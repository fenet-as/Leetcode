class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = []

        cs = 0
        for e in nums:
            cs += e
            res.append(cs)
        return res
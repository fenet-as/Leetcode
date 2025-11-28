class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        sa = sorted(nums)

        hm = {}
        for i,e in enumerate(sa):
            if e not in hm:
                hm[e] = i

        res = []
        for e in nums:
            res.append(hm[e])


        return res


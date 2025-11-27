class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_hm = {}

        for i in range(len(nums)):
            if (target - nums[i]) in seen_hm:
                return [i,seen_hm[target-nums[i]]]
            seen_hm[nums[i]] = i
         
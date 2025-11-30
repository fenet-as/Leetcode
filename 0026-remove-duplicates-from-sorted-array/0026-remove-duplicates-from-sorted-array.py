class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        h = 0
        for j in range(1,len(nums)):
            if nums[j] != nums[h]:
                h += 1
                nums[h] = nums[j]

        return h+1
        
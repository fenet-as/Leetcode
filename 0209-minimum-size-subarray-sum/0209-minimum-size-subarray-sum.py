class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        '''
        dsw
        expand untill sum >= target
        when the sum is >= target i shrink
        and track the size

        '''

        min_size = float('inf')
        cs = 0
        i = 0
        for j in range(len(nums)):
            cs += nums[j]
            while cs >= target:
                min_size = min(min_size, j-i+1)
                cs -= nums[i]
                i += 1
                
        if min_size == float('inf'):
            return 0
        return min_size


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        '''
        '''
        cs = 0
        i = 0
        mn = float('inf')
        for j in range(len(nums)):
            cs += nums[j]
            while cs >= target:
                mn = min(mn,j-i+1)
                cs -= nums[i]
                i += 1
        
        if mn == float('inf'):
            return 0
        return mn
    
        
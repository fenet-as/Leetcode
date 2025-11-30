class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        '''
        sort
        ssw of size k 
        find the d/ce i and the j index values
        min the diffence

        '''

        nums.sort()


        i = 0
        diff = float('inf')
        for j in range(k-1,len(nums)):
            d =  nums[j] - nums[i]
            diff = min(diff,d)
            i += 1
        return diff

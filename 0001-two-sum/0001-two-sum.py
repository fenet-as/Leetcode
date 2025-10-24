class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''

        '''
        hm = {}
        for i,v in enumerate(nums):
            tv = target - v
            if tv in hm:
                return [hm[tv],i]
            hm[v]=i
        

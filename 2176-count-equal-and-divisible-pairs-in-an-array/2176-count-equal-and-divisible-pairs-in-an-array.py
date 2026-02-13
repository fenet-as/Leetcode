class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        indices = defaultdict(list)

        count = 0
        for i in range(len(nums)):
            ind = indices[nums[i]]
            for j in range(len(ind)):
                if (ind[j]*i) % k == 0:
                    count += 1
            indices[nums[i]].append(i)
        return count
            

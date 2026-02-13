class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        count = Counter(nums)

        dom = -1
        for e in count:
            if count[e] > (len(nums)//2):
                dom = e
                break

        
        ct = 0
        for i in range(len(nums)):
            if nums[i] == dom:
                ct += 1
                count[dom] -= 1

            if ct > ((i+1)//2) and count[dom] > ((len(nums)-(i+1))//2):
                return i
        return -1



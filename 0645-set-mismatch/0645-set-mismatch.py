class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:

        tn = []
        for i in range(len(nums)):
            tn.append(i+1)
        nums.sort()

        st = set(tn)

        res = []

        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                res.append(nums[i])
                break
        for e in nums:
            if e in st:
                st.remove(e)
        for e in st:
            res.append(e)
        
        
        return res
        
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        hm = {}
        arr = []
        for i,v in enumerate(nums):
            arr.append((i,v))
        
        nums.sort()
        st = set()

        for i in range(len(nums)-1):
            if nums[i] not in st:
                st.add(nums[i])
                hm[nums[i]] = i
        if nums[-1] not in st:
            hm[nums[-1]] = len(nums)-1
            
        res = []

        for e in arr:
            ei = e[0]
            ev = e[1]
            res.append(hm[ev])


        return res    




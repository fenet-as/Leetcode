class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
            
        '''
        nums1 = [4,1,2], nums2 = [1,3,4,2]

        2,4,3,1

        hm = {}
        ce = st.pop()
        while st and st[-1] < ce:
            st.pop()
        if st:
            hm[ce] = st[-1]
        else:
            hm[ce] = -1

        

        '''

        hm = {}
        for e in nums2:
            hm[e] = -1
        nums2.reverse()
        st = nums2


        while st:
            ce = st.pop()
            ci = len(st)-1
            while ci >= 0 and st[ci] < ce:
                ci -= 1
            if ci >= 0:
                hm[ce] = st[ci]
            else:
                hm[ce] = -1
        res = []
        for e in nums1:
            res.append(hm[e])
        return res


            
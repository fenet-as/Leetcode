class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        res = []

        for i in range(len(l)):
            s = l[i]
            e = r[i]

            st = nums[s:e+1]
            st.sort()
            asm = True
            d = st[1]-st[0] 

            for j in range(len(st)-1):
                if (st[j+1] - st[j]) != d:
                    asm = False
                    res.append(asm)
                    break
            else:
                res.append(asm)
                
        return res


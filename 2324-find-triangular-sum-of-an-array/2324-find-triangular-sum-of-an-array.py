class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        st = nums


        while len(st) > 1:
            ns = []
            n = len(st)-1
            for i in range(n):
                sm = (st[i] + st[i+1]) % 10
                ns.append(sm)
                i += 1
            st = ns
         
        return st[-1]




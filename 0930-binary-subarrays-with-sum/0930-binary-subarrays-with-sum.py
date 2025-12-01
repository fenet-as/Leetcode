class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        '''

        sm[j] - sm[i] = k

        sm[i] --hm

        sm[j] -k in hm, ct ++
        '''

        ps = [0]

        cs = 0

        for e in nums:
            cs += e
            ps.append(cs)
        

        hm = defaultdict(int)
        ct = 0
        for e in ps:
            if e-goal in hm:
                ct += hm[e-goal]
            hm[e] += 1

            
        return ct




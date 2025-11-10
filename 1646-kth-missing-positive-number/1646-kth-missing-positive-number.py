from collections import Counter
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        arm = []

        hm = Counter(arr)
        mx = max(arr)
        ct = 0

        for i in range(1,mx+1):
            if i not in hm:
                arm.append(i)
                ct += 1
                if ct > k-1:
                    return arm[k-1]
        nm = mx+1
        while len(arm) <= k:
            arm.append(nm)
            nm += 1
        return arm[k-1]
        
                   
        
        

        




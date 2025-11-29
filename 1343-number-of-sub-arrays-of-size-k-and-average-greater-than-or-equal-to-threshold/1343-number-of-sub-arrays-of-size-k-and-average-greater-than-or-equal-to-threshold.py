class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        cs = 0
        ct = 0
        for i in range(k):
            cs += arr[i]
        if (cs/k) >= threshold:
            ct += 1
        i = 0
        for j in range(k,len(arr)):
            cs += arr[j]
            cs -= arr[i]
            i += 1
            if (cs/k) >= threshold:
                ct += 1
        return ct
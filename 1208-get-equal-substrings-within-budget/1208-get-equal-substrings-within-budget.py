class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        '''
        expand when cc < maxcost 
        '''
        
        i = 0
        c = 0
        mx = 0
        for j in range(len(s)):
            c += abs( ord(s[j]) - ord(t[j]) )
            while c > maxCost:
                c -= abs(ord(s[i]) - ord(t[i]) )
                i += 1
            mx = max(mx,j-i+1)
        return mx
            

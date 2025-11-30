class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        
        i = 0
        exp = 0
        mx = 0
        for j in range(len(s)):
            exp += abs(ord(t[j]) - ord(s[j]) )
            while exp > maxCost:
                exp -= abs(ord(t[i]) - ord(s[i]) )
                i += 1
            mx = max(mx,j-i+1)
        return mx
            


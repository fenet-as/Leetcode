class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        mx = 0
        j = 0
        for i in range(len(s)):
            while s[i] in seen:
                seen.remove(s[j])
                j += 1
            seen.add(s[i])
            mx = max(mx,i-j+1)


        
        return mx
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        w = set()

        i = 0
        mx = 0
        for j in range(len(s)):
            while s[j] in w:
                w.remove(s[i])
                i += 1
            w.add(s[j])
            mx = max(mx,j-i+1)
        return mx
        
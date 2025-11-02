class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        da -
        shrink whne there is reap char
        else expand and track the max size

        w = set
        loop through str
        when e not in w add it to w
        when e in win, shrink untill e is not in the set

        '''

        w = set()
        mx = 0
        i = 0
        for j in range(len(s)):
            while s[j] in w:
                w.remove(s[i])
                i += 1
            w.add(s[j])
            mx = max(mx,j-i+1)
        return mx

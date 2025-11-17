class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()
        g.sort()

        ct = 0
        i = 0
        j = 0
        while i < len(g) and j < len(s):
            while  i < len(g) and j < len(s) and g[i] > s[j]:
                j += 1 
            if j < len(s):
                ct += 1
            
            i += 1
            j += 1
        return ct


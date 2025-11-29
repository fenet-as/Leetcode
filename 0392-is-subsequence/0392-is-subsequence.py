class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0

        ls = len(s)
        lt = len(t)


        for j in range(lt):
            if i < ls and t[j] == s[i]:
                i += 1
            elif i >= ls:
                break
        
        if i >= len(s):
            return True
        return False
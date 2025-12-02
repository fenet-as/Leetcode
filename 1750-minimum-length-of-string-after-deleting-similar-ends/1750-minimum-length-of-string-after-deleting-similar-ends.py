class Solution:
    def minimumLength(self, s: str) -> int:
        i = 0
        j = len(s)-1

        while i < j:

            if s[i] == s[j]:
                while i < len(s) and j >= 0 and s[i] == s[j]:
                    i += 1
                i -= 1
                while i < len(s) and j >= 0 and  s[i] == s[j]:
                    j -= 1
                j += 1

                i += 1
                j -= 1
            else:
                break
        ln = j-i+1

        if ln < 0:
            return 0
        return (j - i +1)




class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s)-1

        re = False
        fla = True
        while i < j:
            if s[i] != s[j]:
                if not re:
                    i += 1
                    re = True
                else:
                    fla = False
                    break
            else:
                i += 1
                j -= 1
        
        i = 0
        j = len(s)-1

        re2 = False
        sla = True
        while i < j:
            if s[i] != s[j]:
                if not re2:
                    j -= 1
                    re2 = True
                else:
                    sla = False
                    break
            else:
                i += 1
                j -= 1
            
        return fla or sla
        





        
        
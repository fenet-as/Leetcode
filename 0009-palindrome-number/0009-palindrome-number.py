class Solution:
    def isPalindrome(self, x: int) -> bool:
        strn = str(x)

        i = 0
        j = len(strn) - 1

        while i <= j:
            if strn[i] != strn[j]:
                return False
            i += 1
            j -= 1
        return True
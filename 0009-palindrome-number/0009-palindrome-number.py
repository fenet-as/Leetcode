class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        arr = []

        for e in str(x):
            arr.append(e)
        
        return arr == arr[::-1]
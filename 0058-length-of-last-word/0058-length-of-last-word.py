class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        nn = s.split()
        return len(nn[-1])
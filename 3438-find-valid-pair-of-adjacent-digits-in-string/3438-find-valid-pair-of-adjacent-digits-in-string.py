class Solution:
    def findValidPair(self, s: str) -> str:
        
        s_count = Counter(s)

        for i in range(len(s)-1):
            
            if (s_count[s[i]] == int(s[i])) and (s_count[s[i+1]] == int(s[i+1])):
                if s[i] != s[i+1]:
                    return s[i:i+2]
        return ""

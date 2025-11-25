class Solution:
    def reverseVowels(self, s: str) -> str:
        
        sl = list(s)
        vowels = set('aeiouAEIOU')

        i = 0
        j = len(s)-1

        while i < j:
            while i < j and sl[i] not in vowels:
                i += 1
            while i < j and sl[j] not in vowels:
                j -= 1
            
            if i < j:
                sl[i],sl[j] = sl[j],sl[i]
            i += 1
            j -= 1
        
        return ''.join(sl)

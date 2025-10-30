class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        def rc1(word):
            r1 = {'q','w','e','r','t','y','u','i','o','p'}
            for e in word:
                e = e.lower()
                if e not in r1:
                    return False
            return True
        
        def rc2(word):
            r2 = {'a','s','d','f','g','h','j','k','l'}
            for e in word:
                e = e.lower()
                if e not in r2:
                    return False
            return True

        def rc3(word):
            r3 = {'z','x','c','v','b','n','m'}
            for e in word:
                e = e.lower()
                if e not in r3:
                    return False
            return True

        res = []
        for e in words:
            if rc1(e) or rc2(e) or rc3(e):
                res.append(e)
        return res

            
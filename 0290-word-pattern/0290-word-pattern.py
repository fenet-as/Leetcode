class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        map = {}

        words = s.split()

        seen = set()

        if len(pattern) != len(words):
            return False
        for i in range(len(pattern)):

            if pattern[i] not in map:
                if words[i] in seen:
                    return False
                map[pattern[i]] = words[i]
                seen.add(words[i])
            else:
                if words[i] != map[pattern[i]]:
                    return False
        return True
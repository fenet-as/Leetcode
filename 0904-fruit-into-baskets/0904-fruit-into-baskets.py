from collections import defaultdict
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        hm = defaultdict(int)
        i = 0
        mx = 0
        for j in range(len(fruits)):
            hm[fruits[j]] += 1
            while len(hm)>2:
                hm[fruits[i]] -= 1
                if hm[fruits[i]] == 0:
                    del hm[fruits[i]]
                i += 1
            mx = max(mx,j-i+1)
        return mx
            
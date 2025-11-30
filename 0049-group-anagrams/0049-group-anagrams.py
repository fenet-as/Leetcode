class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = defaultdict(list)

        for w in strs:
            sorted_w = ''.join(sorted(list(w)))
            hm[sorted_w].append(w)

        res = []
        for e in hm:
            res.append(hm[e])
        return res



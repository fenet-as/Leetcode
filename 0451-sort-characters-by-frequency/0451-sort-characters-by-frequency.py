class Solution:
    def frequencySort(self, s: str) -> str:
        s_count = Counter(s)

        list_s = list(s)
        list_s.sort(key = lambda x:(s_count[x],ord(x)),reverse=True)

        return ''.join(list_s)
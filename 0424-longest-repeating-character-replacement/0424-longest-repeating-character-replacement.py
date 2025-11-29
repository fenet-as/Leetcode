class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hm = {}

        i = 0
        mx = 0
        mxf = 0
        for j in range(len(s)):
            if s[j] not in hm:
                hm[s[j]] = 1
            else:
                hm[s[j]] += 1

            mxf = max(mxf,hm[s[j]])

            while (j-i+1) - mxf > k:
                hm[s[i]] -= 1
                if hm[s[i]] == 0:
                    del hm[s[i]]
                i += 1
            mx = max(mx,j-i+1)

        return mx
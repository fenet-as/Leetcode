class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st = set(nums)
        longest = 0

        for x in st:
            if x - 1 not in st:
                curr = x
                length = 1

                while curr + 1 in st:
                    curr += 1
                    length += 1

                longest = max(longest, length)

        return longest

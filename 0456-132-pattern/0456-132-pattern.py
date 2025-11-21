class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []      
        second = float('-inf')

        for n in reversed(nums):
            if n < second:
                return True

            while stack and n > stack[-1]:
                second = stack.pop()

            stack.append(n)
        return False

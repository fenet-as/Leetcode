class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stack = []
        for e in asteroids:
            if e > 0:
                stack.append(e)
            else:
                while stack and stack[-1] > 0 and stack[-1] < abs(e):
                    stack.pop()
                if stack and stack[-1] > 0 and stack[-1] > abs(e):
                    continue
                elif stack and stack[-1] > 0 and stack[-1] == abs(e):
                    stack.pop()
                    continue
                stack.append(e)
        return stack

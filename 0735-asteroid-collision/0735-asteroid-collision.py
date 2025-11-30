class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for e in asteroids: #(O(n))
            if e > 0:
                stack.append(e)
            else:
                if stack and stack[-1] < 0:
                    stack.append(e)
                elif stack and stack[-1] == abs(e):
                    stack.pop() 
                    continue

                else:
                    while stack and stack[-1] > 0 and stack[-1] < abs(e):
                        stack.pop()
                    if stack and stack[-1] > 0 and stack[-1] > abs(e):
                        continue
                    elif stack and stack[-1] > 0 and stack[-1] == abs(e):
                        stack.pop()
                        continue
                    else:
                        stack.append(e)
        return stack
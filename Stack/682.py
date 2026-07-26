class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for o in operations:
            if o == '+' and len(stack) >= 2:
                x = stack[-1]
                y = stack[-2]
                z = x + y
                stack.append(z)
            elif o == 'D' and len(stack) > 0:
                x = stack[-1]
                z = x*2
                stack.append(z)
            elif o == 'C' and len(stack) > 0:
                stack.pop()
            else:
                stack.append(int(o))

        return sum(stack)

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = { '+', '-', '*', '/' }
        for i in range(len(tokens)):
            if tokens[i] in ops:
                y = int(stack.pop())
                x = int(stack.pop())
                op = tokens[i]
                match op:
                    case '+':
                        z = x + y
                        stack.append(z)
                    case '-':
                        z = x - y
                        stack.append(z)
                    case '*':
                        z = x * y
                        stack.append(z)
                    case '/':
                        z = x / y
                        stack.append(int(z))
            else:
                stack.append(int(tokens[i]))

        return stack[0]



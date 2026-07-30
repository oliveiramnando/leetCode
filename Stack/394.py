class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for c in s:
            if c == ']':
                encoded_string = ''
                while stack and stack[-1] != '[':
                    d = stack.pop()
                    encoded_string = d + encoded_string

                ob = stack.pop()
                print(ob) # should print '['
                
                num = ''
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num

                k = int(num)

                encoded_string = encoded_string * k
                stack.append(encoded_string)

            else:
                stack.append(c)
        

        return ''.join(stack)

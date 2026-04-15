class Solution:
    def isValid(self, s: str) -> bool:
        stack = [0]

        for c in s:
            if (c == ")" and stack[-1] == "(") or ( c == "}" and stack[-1] == "{") or ( c == "]" and stack[-1] == "["):
                stack.pop()
            
            else:
                stack.append(c)
        
        return len(stack) == 1

            
        

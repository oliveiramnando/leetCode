class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char != "]": #keep adding until we hit "]"
                stack.append(char)
            else: 
                curr_str = ""
                while stack[-1] != "[": # working top of stack until "["
                    curr_str = stack.pop() + curr_str
                stack.pop() # pops "["
                curr_num = ""
                while stack and stack[-1].isdigit(): # read the number until end of stack/ we hit a char
                    curr_num = stack.pop() + curr_num
                curr_str = int(curr_num) * curr_str 
                stack.append(curr_str) #add it so the stack
        
        return "".join(stack)

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in range(len(s)):
            if stack: # if stack has some parenthesis 
                last = stack[-1] # check the lates parenthesis
                if self.is_pair(last, s[i]): # check the latest and current to see if they are a pair
                    stack.pop() #if it is pop it off stack and continue
                    continue
            stack.append(s[i]) # if nothing on stack or if not a pair add to stack
        
        return not stack
   
    def is_pair(self, last, curr): #checks if pair
        if last =="(" and curr == ")" or last =="{" and curr == "}" or last =="[" and curr == "]":
            return True
        return False

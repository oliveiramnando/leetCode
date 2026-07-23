class Solution:
    def validPalindrome(self, s: str) -> bool:
        if len(s) < 3:
            return True

        txt = []
        for c in s:
            txt.append(c)

        txt1 = txt.copy()
        txt2 = txt.copy()
        l, r = 0, len(txt) - 1
        
        while l < r and txt[l] == txt[r]: # should find the first mismatch, if not then it is palindrome
            l += 1
            r -= 1
        
        if l >= r:
            return True
        
        # we can use l and r to just deleted d
        del txt1[l]
        del txt2[r]
        if (txt1 == txt1[::-1]) or (txt2 == txt2[::-1]):
            return True

        return False    
   

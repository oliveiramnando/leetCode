class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        
        final = [0] * 26 

        for i in range(len(s)):
            final[ord(s[i]) - ord('a')] += 1
            final[ord(t[i]) - ord('a')] -= 1


        for i in range(len(final)):
            if final[i] != 0:
                return False
        
        return True

        
        

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        c1, c2 = 0, 0
        len1, len2 = len(word1), len(word2)

        mergedString= ""

        while c1 < len1 and c2 < len2:
            mergedString += word1[c1]
            mergedString += word2[c2]
            
            c1 += 1
            c2 += 1

        while c1 < len1:
            mergedString += word1[c1]        
            c1 += 1

        while c2 < len2:
            mergedString += word2[c2]        
            c2 += 1
            
        return mergedString

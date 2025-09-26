class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        pref = strs[0]
        pref_len = len(pref) 

        for s in strs[1:]: #starts from second word
            while pref != s[0:pref_len]: # while loop shortens pref until it matches
                pref_len -= 1
                if pref_len == 0:
                    return ""
                pref = pref[0:pref_len]
        
        return pref

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ""

        prefix = strs[0]
        prefix_len = len(prefix)

        for string in strs[1:]:
            while prefix != string[0:prefix_len]:
                prefix_len -= 1
                if prefix_len == 0:
                    return ""
        
                prefix = prefix[0:prefix_len]
        return prefix


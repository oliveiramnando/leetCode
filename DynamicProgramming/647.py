class Solution:
    def countSubstrings(self, s: str) -> int:
        numPalin = 0

        def expand_around_center(s: str, left: int, right: int):
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            return count
        
        for i in range(len(s)):
            odd = expand_around_center(s, i, i)
            even = expand_around_center(s, i, i + 1)
            numPalin += (odd + even)
        
        return numPalin

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:
            return []

        res = []
        ss_count = {} # substring count

        substring = ""
        for i in range(10):
            substring = substring + s[i]
        
        ss_count[substring] = 1 + ss_count.get(substring, 0)
        left = 1
        for right in range(10, len(s)):
            substring = s[left:right] + s[right]
            ss_count[substring] = 1 + ss_count.get(substring, 0)
            left += 1

        for string in ss_count:
            if ss_count.get(string) > 1:
                res.append(string)

        return res

# ---------- Optimization ---------- #
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        ans, seen = set(), set()
        for i in range(len(s)-9):
            dna = s[i:i+10]
            if dna in seen:
                ans.add(dna)
            else:
                seen.add(dna)
        return list(ans)


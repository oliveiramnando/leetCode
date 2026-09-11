
class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        n = len(digits)
        res = 0
        tracked = set()
        for i in range(n):
            if digits[i] == 0:
                continue
            
            for j in range(n):
                if i == j:
                    continue
                for k in range(n):
                    if j == k or i == k:
                        continue
                    if digits[k] % 2 == 0:
                        num = int(str(digits[i]) + str(digits[j]) + str(digits[k]))
                        if num in tracked:
                            continue
                        tracked.add(num)
                        res += 1
                    
        
        return res

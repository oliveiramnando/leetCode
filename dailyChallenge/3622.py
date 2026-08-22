class Solution:
    def checkDivisibility(self, n: int) -> bool:
        s = str(n)
        digits = []
        for d in s:
            digits.append(int(d))
        
        digitSum = sum(digits)
        digitProd = math.prod(digits)

        if n % (digitSum + digitProd) == 0:
            return True
        
        return False

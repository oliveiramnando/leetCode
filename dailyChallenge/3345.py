class Solution:
    def smallestNumber(self, n: int, t: int) -> int:

        while n < 10 and n % t != 0:
            n += 1
            if n % t == 0:
                return n
        
        ones = n % 10
        tens = n // 10
        prod = tens * ones
        
        while prod % t != 0:
            n += 1
            tens = n // 10
            ones = n % 10
             
            prod = tens * ones

        return n


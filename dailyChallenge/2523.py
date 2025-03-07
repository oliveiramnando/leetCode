class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:

        found = self.SieveOfEratosthenes(left, right)

        if len(found) < 2:
            return [-1, -1]

        min = float('inf')

        print(found)

        closest = [right, right]

        for i in range(1, len(found)):

            diff = found[i] - found[i - 1]

            if diff < min:
                min = diff
                closest = [found[i-1], found[i]]

        return closest

    def SieveOfEratosthenes(self, left: int, right: int) -> List[int]:
        pList = []

        prime = [True for i in range(right + 1)]
        p = 2
        while (p * p <= right):

            if (prime[p] == True):
                for i in range(p * p, right + 1, p):
                    prime[i] = False
            p += 1

        for p in range(2, right + 1):
            if prime[p] and p > left - 1:
                pList.append(p)
        
        return pList

        

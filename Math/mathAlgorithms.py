
def SieveOfEratosthenes(self, limit: int) -> List[int]:
    """ Finds all prime numbers until the max"""
    pList = []

    prime = [True for i in range(limit + 1)]
    p = 2
    while (p * p <= limit):

        if (prime[p] == True):
            for i in range(p * p, limit + 1, p):
                prime[i] = False
        p += 1

    for p in range(2, limit + 1):
        if prime[p]:
            pList.append(p)
        
    return pList

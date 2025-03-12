class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:

        hash = set()

        result = [0] * len(A)

        for i in range(len(A)):
            if A[i] == B[i]:
                result[i] += 1 
            else:
                if A[i] in hash:
                    result[i] += 1 
                if B[i] in hash:
                    result[i] += 1
            hash.add(A[i])
            hash.add(B[i])

            if i - 1 >= 0:
                result[i] += result[i-1]
        
        return result

        

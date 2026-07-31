class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr)-1

        while r-l >= k:
            a = arr[l]
            b = arr[r]

            Asub = abs(x-a)
            Bsub = abs(x-b)
            if Asub <= Bsub:
                r -= 1
            else:
                l += 1


        return arr[l:r+1]
        


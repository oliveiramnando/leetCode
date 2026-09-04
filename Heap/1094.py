
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda t: t[1])

        minHeap = []
        currPass = 0

        for pool in trips:
            numPass, start, end = pool
            currPass += numPass

            heapq.heappush(minHeap, [end, numPass])

            top = minHeap[0][0]
            while top <= start:
                getOff, passOff = heapq.heappop(minHeap)
                currPass -= passOff
                top = minHeap[0][0] 

            if currPass > capacity:
                return False
        
        return True


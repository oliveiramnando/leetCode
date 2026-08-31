class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-n for n in stones] 
        heapq.heapify(heap)

        while len(heap) > 1:
            y = -(heapq.heappop(heap))
            x = -(heapq.heappop(heap))

            smash = y - x
            if smash != 0:
                heapq.heappush(heap, -(smash))

        return -(heap[0]) if heap else 0

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-s for s in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            a = -heapq.heappop(maxHeap)
            b = -heapq.heappop(maxHeap)

            if a != b:
                heapq.heappush(maxHeap, -(a - b)) 

        return -maxHeap[0] if maxHeap else 0   

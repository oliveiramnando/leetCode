class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []

        for n in nums:
            heapq.heappush(minHeap, n)
            if len(minHeap) > k:
                heapq.heappop(minHeap)

        return heapq.heappop(minHeap)

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        heapq.heapify(heap)

        for n in nums:
            heapq.heappush(heap, n)

            if len(heap) > k:
                heapq.heappop(heap)

        return heap[0]
        

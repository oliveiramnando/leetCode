class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(x, y):
            return math.sqrt((x**2) + (y**2))
            
        res = []
        minHeap = []
        for x, y in points:
            d = dist(x, y)
            heapq.heappush(minHeap, (d, [x, y]))

        for _ in range(k):
            d, pair = heapq.heappop(minHeap)
            res.append(pair)

        return res

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        heapq.heapify(heap)

        for x, y in points:
            dis = self.dfo(x,y)
            heapq.heappush(heap, [-dis, [x, y]])
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        for dis, points in heap:
            res.append(points)

        return res


    def dfo(self, x, y): 
        return math.sqrt((x*x) + (y*y))

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

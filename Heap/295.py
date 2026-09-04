class MedianFinder:

    def __init__(self):
        self.small = []     # max Heap
        self.large = []     # min Heap

    def addNum(self, num: int) -> None:
        # if num is larger than the smallest of the bigger half, insert in large
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        
        # otherwise insert into small
        else:
            heapq.heappush(self.small, -1 * num)
        
        # rebalance the heap if difference is more than one by moving top of one heap into the other
        if abs(len(self.small) - len(self.large)) > 1:
            if len(self.small) > len(self.large):
                num = heapq.heappop(self.small)
                heapq.heappush(self.large, -1 * num)
            else:
                num = heapq.heappop(self.large)
                heapq.heappush(self.small, -1 * num)

    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            small = -(self.small[0])
            large = self.large[0]
            return (small + large)/2
        
        if len(self.small) > len(self.large):
            return -(self.small[0])
        else:
            return self.large[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


class MedianFinder:

    def __init__(self):
        self.small, self.large = [], []
        

    def addNum(self, num: int) -> None:
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -1 * num)
        
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)
        

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        return (-1 * self.small[0] + self.large[0]) / 2.0

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

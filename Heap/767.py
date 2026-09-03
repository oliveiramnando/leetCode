
class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        res = []
        maxHeap = []
        for char, cnt in count.items():
            heapq.heappush(maxHeap, [-cnt, char])
        
        prevChar = ""
        prevCnt = 0
        
        while maxHeap:
            cnt, char = heapq.heappop(maxHeap)

            res.append(char)
            cnt += 1

            if prevCnt < 0:
                heapq.heappush(maxHeap, [prevCnt, prevChar])
            
            prevCnt = cnt
            prevChar = char

        if prevCnt < 0:
            return ""
            a
        return "".join(res)

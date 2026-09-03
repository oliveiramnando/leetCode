
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        maxHeap = []

        if a:
            heapq.heappush(maxHeap, [-a, 'a'])
        if b:
            heapq.heappush(maxHeap, [-b, 'b'])
        if c:
            heapq.heappush(maxHeap, [-c, 'c'])

        res = []

        while maxHeap:
            cnt, char = heapq.heappop(maxHeap)

            # Can't use char because it would make xxx
            if len(res) >= 2 and res[-1] == char and res[-2] == char:
                if not maxHeap:
                    break

                cnt2, char2 = heapq.heappop(maxHeap)

                res.append(char2)
                cnt2 += 1

                if cnt2 < 0:
                    heapq.heappush(maxHeap, [cnt2, char2])

                heapq.heappush(maxHeap, [cnt, char])

            else:
                res.append(char)
                cnt += 1

                if cnt < 0:
                    heapq.heappush(maxHeap, [cnt, char])

        return "".join(res)

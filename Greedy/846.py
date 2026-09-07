
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        minHeap = []
        for n in hand:
            heapq.heappush(minHeap, n)
        
        while minHeap:
            prev = heapq.heappop(minHeap)
            size = 1
            equalCards = []
            while minHeap and size < groupSize:
                card = heapq.heappop(minHeap)
                if card == prev:
                    equalCards.append(card)
                    continue

                if prev + 1 != card:
                    return False
                prev = card
                size += 1

            if size < groupSize:
                return False
                
            for c in equalCards:
                heapq.heappush(minHeap, c)

        return True




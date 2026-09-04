

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        maxHeap = []   # maxHeap for current project profits
        projects = []
        n = len(profits)

        for i in range(n):
            projects.append([capital[i], profits[i]])
        
        projects.sort()

        i = 0
        while i < n and k > 0:
            capital, profit = projects[i]
            if not maxHeap and projects[i][0] > w:
                break

            # add all profits we currently have access to the maxHeap
            while capital <= w:
                heapq.heappush(maxHeap, -profit)
                i += 1
                if i < n:
                    capital, profit = projects[i]
                else:
                    break

            # capital and profit should now be pointed to the next project we currently don't have access to; so we take the most profit and add it to our capital until we are able to access the next point of capital
            while maxHeap and k > 0:
                mostProfit = -(heapq.heappop(maxHeap))
                w += mostProfit
                k -= 1 # decrement the amount of projects we have left
                if w >= capital:
                    break

        # make the most profit while you still have projects left
        while maxHeap and k > 0:
            mostProfit = -(heapq.heappop(maxHeap))
            w += mostProfit
            k -= 1 # decrement the amount of projects we have left

        return w



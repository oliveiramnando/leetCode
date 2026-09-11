
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        n = len(intervals)
        res = []
        i = 1
        res.append(intervals[0])
        while i < n:
            if intervals[i][0] > res[-1][1]:
                res.append(intervals[i])
                i += 1    
            while i < n and res[-1][1] >= intervals[i][0]:
                res[-1][1] = max(res[-1][1], intervals[i][1])
                i += 1
            
        return res




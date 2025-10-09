class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i = 0
        n = len(intervals)
        sI, eI = newInterval

        while i < n and intervals[i][1] < sI:
            res.append(intervals[i])
            i += 1
        
        while i < n and intervals[i][0] <= eI:
            sI = min(sI, intervals[i][0])
            eI = max(eI, intervals[i][1])
            i += 1
        res.append([sI, eI])
        
        while i < n:
            res.append(intervals[i])
            i += 1
        
        return res

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []
        intervals.sort(key=lambda x: x[0]) # Sort based on start times

        prev = intervals[0] # intitialize prev with first interval. Will be compared with. Base line for merging process
        for interval in intervals[1:]: # iterate starting from second interval
            if interval[0] <= prev[1]: # check if start time of current interval is less than or equal to end time of prev
                prev[1] = max(prev[1], interval[1]) # Merge intervals to be max end time between the two
            else: # non overlapping
                merged.append(prev)
                prev = interval
        merged.append(prev) # add last interval
        return merged

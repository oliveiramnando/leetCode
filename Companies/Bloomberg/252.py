class Solution:
    def minMeetingRooms(self, meetings: List[List[int]]) -> int:
        if not meetings: return 0
        
        start_times = []
        end_times = []
        
        for [start, end] in meetings:
            start_times.append(start)
            end_times.append(end)
            
        start_times.sort()
        end_times.sort()
        
        j = 0
        num_rooms = 0
        
        for i in range(len(start_times)):
            if start_times[i] < end_times[j]:
                num_rooms += 1
            else:
                end_index += 1
        
        return num_rooms


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i in range(len(tasks)):
            tasks[i].append(i)
            # enqueueTime, processingTime, originalIndex
        tasks.sort()
        # print(tasks)
        availableTasks = [] # this will be a minheap based on processing time
        
        taskPointer = 0
        time = tasks[taskPointer][0] 

        res = []
        while taskPointer < len(tasks) or availableTasks:

            if not availableTasks:
                time = max(time, tasks[taskPointer][0]) # jump foward to next time, without moving backwards in time
                
            while taskPointer < len(tasks) and tasks[taskPointer][0] <= time:
                heapq.heappush(availableTasks, [tasks[taskPointer][1], tasks[taskPointer][2]])
                #                              [processingTime,        originalIndex] 
                taskPointer += 1
        
            if availableTasks:    # CPU available, process next task
                processingTime, taskNumber = heapq.heappop(availableTasks)
                res.append(taskNumber)
                time += processingTime

        return res

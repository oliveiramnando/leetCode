
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        res = [-1, -1]
        idx = []
        prev = head
        curr = head.next
        nxt = head.next.next
        i = 2
        while nxt:
            if prev.val < curr.val > nxt.val or prev.val > curr.val < nxt.val:
                idx.append(i)
            
            i += 1
            prev = curr
            curr = nxt 
            nxt = nxt.next

        if len(idx) < 2:
            return res

        res[1] = idx[-1] - idx[0]
        
        mini = float('inf')
        for i in range(1, len(idx)):
            mini = min(mini, idx[i]-idx[i-1])

        res[0] = mini

        return res


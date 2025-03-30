# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        res = ListNode(0, head)
        p1 = head
        p2 = res

        for _ in range(n):
            p1 = p1.next

        while p1:
            p1 = p1.next
            p2 = p2.next
        
        p2.next = p2.next.next

        return res.next
        

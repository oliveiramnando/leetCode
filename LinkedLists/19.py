# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        ptr = head
        count = 0
        while ptr:
            count += 1
            ptr = ptr.next
        
        if count == 1:
            return None
        
        removal = count - n + 1

        prev = None
        curr = head
        
        for i in range(removal - 1):
            prev = curr
            curr = curr.next

        # if the end
        if curr.next is None:
            prev.next = None
        #if the beginning
        if prev is None:
            head = curr.next
            curr.next = None
        else:
            nxt = curr.next
            curr.next = None
            prev.next = nxt

        return head

# One pass solution:
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        slow = fast = dummy

        for _ in range(n):
            fast = fast.next
        
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next

        return dummy.next


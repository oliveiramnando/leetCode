# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return

        ptr = head
        length = 0
        while ptr is not None:
            length += 1
            ptr = ptr.next
        
        if k >= length:
            k = k % length
            print(k)
        
        if k == 0:
            return head

        l = head
        r = head

        i = 0
        while r.next and i != k:
            r = r.next
            i += 1
        
        while r.next is not None:
            l = l.next
            r = r.next
        
        r.next = head
        head = l.next
        l.next = None

        return head
    


        
        
        

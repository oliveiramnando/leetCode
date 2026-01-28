# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        fast, curr, ptr = head, head, head
        dummy = ListNode(0)
        slow = dummy
        notMultiple = False

        while slow:
            for _ in range(k-1): # setting last node in first list
                if ptr is None or ptr.next is None:
                    notMultiple = True
                    break
                ptr = ptr.next 

            if notMultiple:
                break
                
            slow.next = ptr
            slow = curr

            if ptr is None or ptr.next is None: #window
                fast = None 
            else: 
                fast = ptr.next
            
            ptr = fast 
            while curr != fast: # reversal
                if curr.next is None:
                    nxt = None
                else: 
                    nxt = curr.next

                curr.next = ptr
                ptr = curr
                curr = nxt 
            
            ptr = fast
        
        
        return dummy.next

        

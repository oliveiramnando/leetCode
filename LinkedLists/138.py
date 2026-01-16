"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hash = {None:None}
        cur = head

        # makes copy of nodes and saves into hash for fast lookup
        while cur:
            hash[cur] = Node(cur.val)
            cur = cur.next
        
        # go through list again and set copy node to values of the original
        cur = head
        while cur:
            copy = hash[cur]
            copy.next = hash[cur.next]
            copy.random = hash[cur.random]
            cur = cur.next
        
        return hash[head]
        

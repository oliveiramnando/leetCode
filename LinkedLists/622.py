class ListNode:
    def __init__(self, val=0, prv=None, nxt=None):
        self.val = val
        self.prev = prv
        self.next = nxt

class MyCircularQueue:

    def __init__(self, k: int):
        self.dummy = ListNode(-1)

        self.front = self.dummy
        self.rear = self.dummy

        self.maxCap = k
        self.size = 0

    def enQueue(self, value: int) -> bool:
        if self.size == self.maxCap:
            return False

        node = ListNode(value)

        self.rear.next = node
        node.prev = self.rear
        self.rear = node

        if self.front == self.dummy:
            self.front = node
        
        self.size += 1

        return True

    def deQueue(self) -> bool:
        if self.size == 0:
            return False

        if self.size == 1:
            self.dummy.next = None
            self.front = self.dummy
            self.rear = self.dummy
            self.size -= 1
            return True
        
        curr = self.front

        if curr.next == None:
            curr.prev.next = None
            self.front =  self.rear.prev

        # general case
        else:
            curr.prev.next = curr.next
            curr.next.prev = curr.prev
            self.front = curr.next 

        self.size -= 1
        # if size == 1 after removal, make sure front and rear are the same
        if self.size == 1:
            self.front = self.rear
        
        return True
        

    def Front(self) -> int:
        return self.front.val

    def Rear(self) -> int:
        return self.rear.val
        
    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.maxCap
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()

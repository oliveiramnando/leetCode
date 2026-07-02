class MyHashSet:

    def __init__(self):
        self.data = [False] * 1000001
        
    def add(self, key: int) -> None:
        self.data[key] = True

    def remove(self, key: int) -> None:
        self.data[key] = False

    def contains(self, key: int) -> bool:
        return self.data[key]


class MyHashSet2:

    def __init__(self):
        self.data = [0] * 31251
    
    def getMask(self, key: int) -> int:
        return 1 << (key % 32)
        
    def add(self, key: int) -> None:
        self.data[key // 32] |= self.getMask(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            self.data[key // 32] ^= self.getMask(key)

    def contains(self, key: int) -> bool:
        return self.data[key // 32] & self.getMask(key) != 0


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

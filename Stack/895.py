class FreqStack:

    def __init__(self):
        self.arr = []
        self.dictionary = dict()

    def push(self, val: int) -> None:
        if val not in self.dictionary:
            self.dictionary[val] = 0

        self.dictionary[val] += 1
        self.arr.append(val)

    def pop(self) -> int:        
        highest_val = max(self.dictionary.values())
        all_max_keys = [k for k, v in self.dictionary.items() if v == highest_val]
    
        max_keys_set = set(all_max_keys)

        for i in range(len(self.arr)-1, -1, -1):
            if self.arr[i] in max_keys_set:
                self.dictionary[self.arr[i]] -= 1
                print(self.arr[i])
                return self.arr.pop(i)
        

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()

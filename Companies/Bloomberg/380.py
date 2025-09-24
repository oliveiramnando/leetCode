class RandomizedSet:

    def __init__(self):
        self.values = []
        self.valuesIdx = {} # value: index

    def insert(self, val: int) -> bool:
        if val in self.valuesIdx:
            return False

        self.valuesIdx[val] = len(self.values)
        self.values.append(val)
        return True

    def remove(self, val: int) -> bool: #swap element with the last and delete it so O(1)
        if val not in self.valuesIdx:
            return False
        index = self.valuesIdx[val] # index of element
        self.valuesIdx[self.values[-1]] = index #update last element's postion, with index of element we gonna delete
        del self.valuesIdx[val] # delete element from dict
        self.values[index] = self.values[-1] # moves last element to delete position; doesn't actually swap. just moves last element to where the val u wanna delete is, and pops last index which is a dup of the last element
        self.values.pop() # remove from end

        return True

    def getRandom(self) -> int:
        index = random.randint(0, len(self.values) - 1)
        return self.values[index]

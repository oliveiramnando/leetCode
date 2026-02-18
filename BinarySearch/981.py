class TimeMap:
    def __init__(self):
        self.dictionary = {}


    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.dictionary:
            self.dictionary[key].append([value, timestamp])
        else:
            self.dictionary[key] = [[value, timestamp]]
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dictionary:
            return ""

        keyList = self.dictionary[key]
        res = ""
        l, r = 0, len(keyList)-1

        while l <= r:
            mid = (l + r) // 2
            prevTimestamp = keyList[mid][1]

            if prevTimestamp <= timestamp:
                l = mid + 1
                res = keyList[mid][0]
            else:
                r = mid - 1

        return res
    


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

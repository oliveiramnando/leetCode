class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = {}
 
        for c in word:
            if c not in freq:
                freq[c] = 0
            freq[c] += 1

        res = 0
        r = 1
        while freq:
            remapCount = 0
            for i in range(8):
                if not freq:
                    break
                mostUsed = max(freq, key=freq.get)
                remapCount += freq.pop(mostUsed)

            res += (remapCount * r)
            r += 1

        return res



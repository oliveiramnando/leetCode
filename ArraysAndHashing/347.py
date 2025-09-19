class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {} 
        res = []
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        freqSort = sorted(freq.items(), key=lambda item: item[1], reverse=True)
        for i in range(k):
            res.append(freqSort[i][0])
        return res

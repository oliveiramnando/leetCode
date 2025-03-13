# ---------- First Approach ---------- #
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        result = [0] * len(boxes)

        for i in range(len(boxes)):
            for j in range(len(boxes)):
                if j == i:
                    continue

                if boxes[j] == "1":
                    result[i] += abs(i-j)

        return result

# ---------- Optimization ---------- #


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        relation = dict()
        for i in range(1, n+1):
            relation[i] = set()

        for a, b in trust:
            relation[a].add(b)
        
        judge = []
        for key, value in relation.items():
            if len(value) == 0:
                judge.append(key)
        
        if len(judge) != 1:
            return -1
        
        for key, val in relation.items():
            print(val)
            if key != judge[0] and judge[0] not in val :
                return -1
            
        return judge[0]

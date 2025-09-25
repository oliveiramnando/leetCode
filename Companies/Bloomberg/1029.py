class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        l = sorted(costs, key=lambda x: x[0] - x[1]) #sort based on cost, left half will be towards one city, right half will be towards other city
        cityA = 0 #track of sums
        cityB = 0
        for i in range(len(l) // 2):
            cityA += l[i][0] 
        for i in range(len(l) // 2, len(l)):
            cityB += l[i][1]

        return cityA + cityB

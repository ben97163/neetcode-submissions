class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        res = 0
        curFuel = 0
        for i in range(len(gas)):
            if curFuel + gas[i] >= cost[i]:
                curFuel += gas[i] - cost[i]
            
            else:
                curFuel = 0
                res = i+1
        
        return res
            
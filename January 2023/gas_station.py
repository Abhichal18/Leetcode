class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # if gas required is greater than the gas we can have return -1
        if sum(cost)>sum(gas):
            return -1
        tank=0
        index=0
        for i in range(len(gas)):
            # add the leftover in tank
            tank+=gas[i]-cost[i]
            # if tank value is less than zero
            # next index might be the required index
            if tank<0:
                # initialize tank again to 0 and index to i+1
                tank=0
                index=i+1
        return index

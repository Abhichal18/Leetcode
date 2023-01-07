class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        # sorting the costs
        costs=sorted(costs)
        count=0
        for i in costs:
            # subtracting the cost of ice bar form max limit
            coins-=i
            # if the spent limit is greater than equal to 0
            # increment the count
            if coins>=0:
                count+=1
            else:
                break
        return count

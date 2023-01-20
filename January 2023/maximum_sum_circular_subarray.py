class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        currMax=nums[0]
        currMin=0
        maxi=nums[0]
        total=sum(nums)
        for i in range(1,len(nums)):
            currMax=max(currMax+nums[i],nums[i])
            currMin=min(currMin+nums[i],nums[i])
            #print(currMax,currMin)
            maxi=max(maxi,currMax,total-currMin)
        return maxi

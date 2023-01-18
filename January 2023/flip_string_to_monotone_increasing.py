class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        ans=0
        # keep count of 1
        count1=0
        for i in s:
            if i=='1':
                count1+=1
            # if number not 1 then decrease the count by 1 as any of this 0 or 
            #previous ones will contribute in. the flipping and increment the ans
            elif count1:
                count1-=1
                ans+=1
        return ans

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans=[]
        index=0
        val1=0
        for i in range(len(intervals)):
            if intervals[i][1]<newInterval[0]:
                ans.append(intervals[i])
                index+=1
            else:
                break
        for i in range(index, len(intervals)):
            if intervals[i][0]<=newInterval[1]:
                newInterval[0]=min(intervals[i][0],newInterval[0])
                newInterval[1]=max(intervals[i][1],newInterval[1])
                index+=1
            else:
                break
        ans.append(newInterval)
        for i in range(index,len(intervals)):
            ans.append(intervals[i])
        return ans

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # sorting the array
        points=sorted(points)
        # initializing the arrow count
        count=0
        prev_end=points[0][1]
        # iterating from first index in point araay
        for i in range(1,len(points)):
            # if the start of diameter of balloon is less than the end
            # it means it overlaps with the diameter of the previous balloon
            # the new prev_end will be the min of current balloons end and prev_end
            if points[i][0]<=end:
                prev_end=min(prev_end,points[i][1])
            # otherwise this balloon doesn't overlap with any previous balloon
            # we increment the count by 1 as previous overlapped balloons need
            # one arrow for themselves and prev_end will be initialized with the
            # end of current balloon
            else:
                count+=1
                prev_end=points[i][1]
        # returning count+1 because we need one arrow for last set of
        # overlapping balloons
        return count+1

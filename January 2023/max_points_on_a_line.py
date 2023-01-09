class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # store the maximum points in a line
        maxi=0
        # iterate over points
        for i in range(len(points)):
            # stores the count of points having similar slopes
            slopes=dict()
            # iterating from i+1th point
            for j in range(i+1,len(points)):
                # calculating the numerator and denominator for slope formula
                numerator=points[j][1]-points[i][1]
                denominator=points[j][0]-points[i][0]
                # if denominator is zero set the slope to infinity else calculate
                if denominator==0:
                    slope=float('inf') 
                else:
                    slope=numerator/denominator
                # if slope in dictionary increment it's count else initialize it to 1
                if slope in slopes:
                    slopes[slope]+=1
                else:
                    slopes[slope]=1
            # get the maximum slope frequency
            maxi=max(maxi,max(slopes.values(),default=0))
        return maxi+1

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        # store removed column count
        count=0
        # iterating the 2-D array columnwise
        for col in range(len(strs[0])):
            for row in range(1,len(strs)):
                # if current character is less than the previous character
                # means the column is not sorted lexicographically
                # hence, increment the count by 1
                if strs[row][col]<strs[row-1][col]:
                    count+=1
                    # no meaning to check for further position so breaking out
                    break
        return count

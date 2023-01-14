from collections import defaultdict
class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        tree=defaultdict(list)
        for i in range(1,len(parent)):
            tree[parent[i]].append(i)
        res=1
        def dfs(current):
            nonlocal res
            left=right=0
            for neighbor in tree[current]:
                neighborL=dfs(neighbor)
                if s[current]!=s[neighbor]:
                    if neighborL>left:
                        right=left
                        left=neighborL
                    elif neighborL>right:
                        right=neighborL
            res = max(res, left+right+1)
            return left+1

        dfs(0)
        return res

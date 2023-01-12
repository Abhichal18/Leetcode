from collections import defaultdict
class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        # to store the tree
        tree = defaultdict(list)
        # storing edges for a node
        for i in edges:
            tree[i[0]].append(i[1])
            tree[i[1]].append(i[0])
        
        # running dfs on the tree
        def dfs(current,parent):
            res = 0
            for node in tree[current]:
                if node != parent:
                    res+=dfs(node,current)
            # if either res is greater than 0 or the node have apple then add 2
            if res or hasApple[current]:
                return res+2
            return res
        return max(dfs(0,-1)-2,0)

from collections import defaultdict
class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        # creating tree using edges
        tree=defaultdict(list)
        for i in edges:
            tree[i[0]].append(i[1])
            tree[i[1]].append(i[0])
        # to store the resultant array
        ans = [0]*n
        # traversing the tree
        def dfs(current, parent, d):
            # keeping the current label count in prev
            if labels[current] in d:
                prev= d[labels[current]]
            else:
                prev=0
            # iterating on neighbors
            for neighbor in tree[current]:
                if neighbor!=parent:
                    dfs(neighbor,current,d)
            # if label is already in dict then increment it else initialize to 1
            if labels[current] in d:
                d[labels[current]]+=1
            else:
                d[labels[current]]=1
            # update the ans with current count -prev count
            ans[current]=d[labels[current]]-prev
        dfs(0,-1,{})
        return ans

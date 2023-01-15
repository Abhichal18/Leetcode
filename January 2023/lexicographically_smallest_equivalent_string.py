from collections import defaultdict
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        # to store the character mappings
        mapping = defaultdict(set)
        for i,j in zip(s1,s2):
            mapping[i].add(j)
            mapping[j].add(i)
        visited=dict()
        # visit array
        for i in mapping:
            visited[i]=False
        cc =[]
        # applying dfs to get the connected components
        def dfs(temp,i,visited):
            visited[i]=True
            temp.add(i)
            for node in mapping[i]:
                if visited[node]==False:
                    temp=dfs(temp,node,visited)
            return temp
                # finding conencted components means getting the chars which are connected to each other
        for i in mapping:
            if visited[i]==False:
                temp=set()
                cc.append(dfs(temp,i,visited))
        # getting the result using the smallest characters from connected components
        ans=''
        for i in baseStr:
            flag=0
            for j in cc:
                if i in j:
                    ans+=min(j)
                    flag=1
                    break
            if flag==0:
                ans+=i
        return ans

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        b_count=dict()
        a =set()
        for i in trust:
            a.add(i[0])
            if i[1] in b_count:
                b_count[i[1]]+=1
            else:
                b_count[i[1]]=1
        for i in b_count:
            if b_count[i]==n-1 and i not in a:
                return i
        if len(a)==0 and n==1:
            return 1
        return -1

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans=[]
        def palindrome(word):
            return word==word[::-1]
        def backtrack(i,cur):
            if i ==len(s):
                ans.append(cur)
                return
            for j in range(i,len(s)):
                sol = s[i:j+1]
                if palindrome(sol):
                    backtrack(j+1,cur+[sol])
        backtrack(0,[])
        return ans            

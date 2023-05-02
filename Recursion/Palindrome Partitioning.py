# leetcode 
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res=[]
        part=[]
        
        def dfs(part,idx):
            if idx>=len(s):
                res.append(part.copy())
                return
            
            for i in range(idx,len(s)):
                if self.isPali(s,idx,i):
                    part.append(s[idx:i+1])
                    dfs(part,i+1)
                    part.pop()
        dfs(part,0)
        return res


    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True

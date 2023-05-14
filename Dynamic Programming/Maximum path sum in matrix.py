class Solution:
    def maximumPath(self, n, mat):
        
        dp=[[-1 for i in range(n+1)] for j in range(n+1)]
        
        def recur(i,j):
            if i<0 or i>=n or j<0 or j>=n:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            dp[i][j]=mat[i][j]+max(recur(i+1,j),recur(i+1,j-1),recur(i+1,j+1))
            return dp[i][j]
            
        res=0
       
        for i in range(n):
            res=max(res,recur(0,i))
        return res

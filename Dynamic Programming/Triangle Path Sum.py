class Solution:
    def minimizeSum(self, n, triangle):
        
        dp=[[float("inf") for i in range(n+1)] for j in range(n+1)]
        for i in range(n):
            for j in range(len(triangle[i])):
                dp[i][j]=-1
        
        
        def dfs(i,j):
            if i==0 and j==0:
                return triangle[0][0]
            if dp[i][j]!=-1:
                return dp[i][j]
            if i<0 or j>=n:
                return float("inf")
            
            dp[i][j]=triangle[i][j]+min(dfs(i-1,j),dfs(i-1,j-1))
            return dp[i][j]
        
        res=float("inf")
        last=triangle[-1]
        for i in range(len(last)):
            res=min(res,dfs(n-1,i))
        return res

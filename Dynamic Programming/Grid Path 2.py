mod=10**9+7
class Solution:
    def totalWays(self, n, m, grid):
        if n==1 and  m==1 and grid[0][0]==1:
            return 0
        
        dp=[[-1 for i in range(m+1)] for j in range(n+1)]
        
        def dfs(i,j):
            
            if i==n-1 and j ==m-1:
                return 1
            if i<0 or i>=n or j<0 or j>=m:
                return 0
            if grid[i][j]==1:
                dp[i][j]=0
                return 0
            
            if dp[i][j]!=-1:
                return dp[i][j]
            
            dp[i][j]=(dfs(i+1,j)+dfs(i,j+1))%mod
            return dp[i][j]%mod
        
        return dfs(0,0)

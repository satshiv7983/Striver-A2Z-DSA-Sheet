
   
class Solution:
    #Function to find total number of unique paths.
    def NumberOfPaths(self,a, b):

        dp=[[-1 for i in range(b)] for j in range(a)]
        def dfs(i,j):
            if i==a-1 or j==b-1:
                return 1
            if i<0 or i>=a or j<0 or j>=b:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            dp[i][j]=dfs(i+1,j)+dfs(i,j+1)
            return dp[i][j]
            
        return dfs(0,0)

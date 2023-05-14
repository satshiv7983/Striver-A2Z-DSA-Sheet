
class Solution:
    def isSubsetSum (self, N, arr, sum):
        dp=[[-1 for i in range(sum+1)] for j in range(N+1)]
        
        def dfs(i,target):
            if target==0:
                return True
            if i<0 or target<0:
                return False
            if dp[i][target]!=-1:
                return dp[i][target]
            dp[i][target]=dfs(i-1,target-arr[i]) or dfs(i-1,target)
            return dp[i][target]
            
        
        return dfs(N-1,sum)
            

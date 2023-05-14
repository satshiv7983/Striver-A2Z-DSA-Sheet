
class Solution:
    def equalPartition(self, N, arr):
        target=sum(arr)
        if target%2!=0:
            return False
        target=target//2
        dp=[[-1 for i in range(target+1)] for j in range(N)]
        
        def dfs(i,target):
            if target==0:
                return True
            if i<=0 or target<0:
                return False
            if dp[i-1][target]!=-1:
                return dp[i-1][target]
            dp[i-1][target]=dfs(i-1,target) or dfs(i-1,target-arr[i-1])
            return dp[i-1][target]
        return dfs(N,target)
            
            

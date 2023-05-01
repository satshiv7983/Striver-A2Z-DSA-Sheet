#User function Template for python3
mod = 10**9+7
from collections import deque
class Solution:
	def perfectSum(self, pat, n, sum):
	    
	    dp = [[0 for i in range(sum + 1)] for j in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = 1
        
        for i in range(1, n + 1):
            for j in range(sum + 1):
                if arr[i - 1] <= j:
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - arr[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]
                dp[i][j]%=mod
        
        return dp[-1][-1] % mod

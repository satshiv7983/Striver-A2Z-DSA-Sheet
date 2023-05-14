class Solution:
	def minDifference(self, arr, n):
		s=sum(arr)
		dp=[[-1 for i in range(s+1)] for j in range(n+1)]
		def dfs(i,target):
		    if target==0:
		        return True
		    if i<0 or target<0:
		        return False
		    if dp[i][target]!=-1:
		        return dp[i][target]
		    
		    dp[i][target]=dfs(i-1,target-arr[i]) or dfs(i-1,target)
		    return dp[i][target]
		
		
		for i in range(s+1):
		    dummy=dfs(n-1,i)
		    
		res=float("inf")
		for i in range(s+1):
		    if dp[n-1][i]==True:
		        res=min(res,abs(i - (s - i)))
		return res

class Solution:
    def minimumEnergy(self, height, n):
        
        if n==1:
            return 0
        dp=[0]*(n+1)
        dp[1]=abs(height[1]-height[0])
        for i in range(2,n):
            dp[i]=min((dp[i-1]+abs(height[i]-height[i-1])),(dp[i-2]+abs(height[i]-height[i-2])))
        return dp[n-1]

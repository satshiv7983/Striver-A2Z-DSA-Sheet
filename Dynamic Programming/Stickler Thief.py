class Solution:  
    
    #Function to find the maximum money the thief can get.
    def FindMaxSum(self,a, n):
        if n==1:
            return a[0]
        dp=[-1]*n
        dp[0]=a[0]
        dp[1]=max(a[0],a[1])
        for i in range(2,n):
            dp[i]=max(a[i]+dp[i-2],dp[i-1])
        return max(dp[n-1],dp[n-2])

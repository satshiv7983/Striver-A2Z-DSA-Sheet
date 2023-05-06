mod=10**9+7
class Solution:
    #Function to count number of ways to reach the nth stair.
    def countWays(self,n):
        
        # bottom up
        # T.C O(n)
        if n is 1:
            return 1
        prev2=1
        prev1=2
        for i in range(2,n):
            cur=(prev2+prev1)%mod
            prev2=prev1
            prev1=cur
        return prev1
            
            
        
        
        
        
        
        
        # top down approach
        # T.C O(n)
        
        # dp=[-1]*(n+1)
        
        # def memo(n):
        #     if n==0 or n==1:
        #         return 1
        #     if dp[n]!=-1:
        #         return dp[n]
            
        #     dp[n]=(memo(n-1)+memo(n-2))%mod
        #     return dp[n]%mod
        # return memo(n)
        

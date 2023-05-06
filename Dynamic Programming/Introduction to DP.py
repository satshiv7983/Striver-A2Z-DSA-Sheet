import sys
sys.setrecursionlimit(10**8)
mod=10**9+7
class Solution:
    def topDown(self, n):
        
        dp=[-1]*(n+1)
        def memo(n):
            if n==0 or n==1:
                return n
            if dp[n]!=-1:
                return dp[n]
            
            dp[n]=(memo(n-1)+memo(n-2))%mod
            return dp[n]%mod
        return memo(n)
    def bottomUp(self, n):
        prev2=0
        prev1=1
        for i in range(n-1):
            cur=(prev2+prev1)%mod
            prev2=prev1
            prev1=cur

        return prev1

import sys
sys.setrecursionlimit(10**8)
class Solution:
    def knapSack(self, N, W, val, wt):
        
        dp=[[-1 for i in range(W+1)] for j in range(N+1)]
        
        def recur(idx,weight):
            if idx<0:
                return 0
            
            if dp[idx][weight]!=-1:
                return dp[idx][weight]
            
            if wt[idx]<=weight:
                dp[idx][weight]=max(val[idx]+recur(idx,weight-wt[idx]),recur(idx-1,weight))
            else:
                dp[idx][weight]=recur(idx-1,weight)
            return dp[idx][weight]
        return recur(N-1,W)

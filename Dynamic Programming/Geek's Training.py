import sys
sys.setrecursionlimit(10**9)
class Solution:
    def maximumPoints(self, points, n):
        
        dp=[[-1 for i in range(4)] for j in range(n+1)]
        
        def memo(idx,cat):
            if idx < 0:
                return 0
            if dp[idx][cat]!=-1:
                return dp[idx][cat]
            
            maxp=-1
            for i in range(3):
                if i!=cat:
                    calc=points[idx][i]+memo(idx-1,i)
                    maxp=max(maxp,calc)
            dp[idx][cat]=maxp
            return dp[idx][cat]
        return memo(n-1,3)

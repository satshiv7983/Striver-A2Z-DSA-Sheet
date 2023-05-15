
class Solution:
    def cutRod(self, price, n):
        
        dp=[[-1 for i in range(n+1)] for j in range(n+1)]
        
        def recur(idx,target):
            if idx==0:
                return target*price[0]
            
            if dp[idx][target]!=-1:
                return dp[idx][target]
            if idx<=target:
                dp[idx][target]=max(price[idx-1]+recur(idx,target-idx),recur(idx-1,target))
            else:
                dp[idx][target]=recur(idx-1,target)
            return dp[idx][target]
            
   
        return recur(n,n)
                
                
                

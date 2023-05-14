mod = 10**9+7
class Solution:
	def perfectSum(self, arr, n, sum):
	    dp=[[-1 for i in range(sum+1)] for j in range(n+1)]
	    def memo(idx,target):
	        if idx == 0:
               if target == 0:
                    if arr[0] == 0:
                        return 2
                    return 1
               if arr[idx] == target:
                   return 1
               return 0
	   
            if dp[idx][target]!=-1:
                return dp[idx][target]
            
            if arr[idx]<=target:
                dp[idx][target]=(memo(idx-1,target-arr[idx])+memo(idx-1,target))%mod
            else:
                dp[idx][target]=memo(idx-1,target)%mod
            return dp[idx][target]%mod
        
        return memo(n-1,sum)

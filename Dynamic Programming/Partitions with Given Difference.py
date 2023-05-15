class Solution:
    def countPartitions(self, n, d, arr):
        mod = int(1e9 + 7)

        def countPartitionsUtil(ind, target, arr, dp):
            if ind == 0:
                if target == 0 and arr[0] == 0:
                    return 2
                if target == 0 or target == arr[0]:
                    return 1
                return 0
            
            if dp[ind][target] != -1:
                return dp[ind][target]
                
            notTaken = countPartitionsUtil(ind-1, target, arr, dp)
            
            taken = 0
            if arr[ind] <= target:
                taken = countPartitionsUtil(ind-1, target-arr[ind], arr, dp)
                
            dp[ind][target] = (notTaken + taken) % mod
            return dp[ind][target]
        
        
        n = len(arr)
        totSum = sum(arr)
        
        # Checking for edge cases
        if totSum - d < 0:
            return 0
        if (totSum - d) % 2 == 1:
            return 0
        
        s2 = (totSum - d) // 2
        
        dp = [[-1 for j in range(s2 + 1)] for i in range(n)]
        return countPartitionsUtil(n-1, s2, arr, dp)

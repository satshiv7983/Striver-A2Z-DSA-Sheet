#User function Template for python3

class Solution:
    def minPartition(self, V):
        deno = [1, 2, 5, 10, 20, 50, 
            100,200, 500,2000]
        n = len(deno)
        
        # Initialize Result
        ans = []
    
        # Traverse through all denomination
        i = n - 1
        while(i >= 0):
            
            # Find denominations
            while (V >= deno[i]):
                V -= deno[i]
                ans.append(deno[i])
    
            i -= 1
        return ans

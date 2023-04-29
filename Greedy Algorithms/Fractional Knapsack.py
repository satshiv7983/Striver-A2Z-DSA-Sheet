class Solution:    
    #Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, W,arr,n):
        
        arr.sort(key=lambda x:(x.value/x.weight),reverse=True)
        res=0
        for i in arr:
            if i.weight<=W:
                res+=i.value
                W-=i.weight
            else:
                res += i.value * W / i.weight
                break
        return res

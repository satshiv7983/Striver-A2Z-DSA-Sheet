class Solution:
    def minCandy(self, N, ratings):
        left=[1]*N
        right=[1]*N
        res=[0]*N
        for i in range(1,N):
            if ratings[i]>ratings[i-1]:
                left[i]=1+left[i-1]
        for i in range(N-2,-1,-1):
            if ratings[i]>ratings[i+1]:
                right[i]=1+right[i+1]
        
        for i in range(N):
            res[i]=max(left[i],right[i])
        return sum(res)

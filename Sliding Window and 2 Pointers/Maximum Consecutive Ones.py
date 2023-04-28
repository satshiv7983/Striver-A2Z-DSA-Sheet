#User function Template for python3

class Solution:
    def longestOnes(self, n, arr, k):
        l,r=0,0
        count=0
        res=0
        while r<n:
            while count==k and arr[r]!=1:
                if arr[l]==0:
                    count-=1
                l+=1
            count+=1 if arr[r]==0 else 0
            res=max(res,r-l+1)
            r+=1
        return res
            

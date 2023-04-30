#User function Template for python3

class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,n,arr,dep):
        arr.sort()
        dep.sort()
        count=1
        res=1
        i,j=1,0
        while i<len(arr) and j<len(dep):
            if arr[i]<=dep[j]:
                count+=1
                i+=1
            else:
                count-=1
                j+=1
            res=max(res,count)
        return res

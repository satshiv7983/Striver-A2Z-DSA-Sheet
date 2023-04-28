#User function Template for python3

class Solution:
    def sumSubarrayMins(self, n, fruits):
        hashmap={}
        l,r=0,0
        res=0
        while r<n:
            while len(hashmap)>=2 and fruits[r] not in hashmap:
                hashmap[fruits[l]]-=1
                if hashmap[fruits[l]]==0:
                    del hashmap[fruits[l]]
                l+=1
            hashmap[fruits[r]]=1+hashmap.get(fruits[r],0)
            res=max(res,r-l+1)
            r+=1
        return res

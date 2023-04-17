class Solution:
    def beautySum(self, s):
        res=0
        n=len(s)
        for i in range(n):
            hashmap={}
            for j in range(i,n):
                hashmap[s[j]]=1+hashmap.get(s[j],0)
                res+=max(hashmap.values())-min(hashmap.values())
        return res
                

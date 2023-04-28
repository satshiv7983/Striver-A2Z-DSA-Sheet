class Solution:
    def characterReplacement(self, s, k):
        n=len(s)
        l,r=0,0
        maxf=0
        res=0
        hashmap={}
        while r<n:
            hashmap[s[r]]=1+hashmap.get(s[r],0)
            maxf=max(maxf,hashmap[s[r]])
            
            if r-l+1-maxf>k:
                hashmap[s[l]]-=1
                l+=1
            res=max(res,r-l+1)
            r+=1
        return res

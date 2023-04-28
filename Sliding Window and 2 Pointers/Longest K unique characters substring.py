
class Solution:

    def longestKSubstr(self, s, k):
        n=len(s)
        hashmap={}
        l,r=0,0
        res=0
        while r<n:
            while len(hashmap)>k:
                hashmap[s[l]]-=1
                if hashmap[s[l]]==0:
                    del hashmap[s[l]]
                l+=1
            hashmap[s[r]]=1+hashmap.get(s[r],0)
            if len(hashmap)==k:
                res=max(res,r-l+1)
            r+=1
        return res if res!=0 else -1
            

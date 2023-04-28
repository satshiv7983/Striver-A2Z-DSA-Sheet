#User function Template for python3

class Solution:
    def longestUniqueSubsttr(self, s):
        n=len(s)
        # sliding window
        freq={}
        l,r=0,0
        res=0
        while r<n:
            while s[r] in freq:
                del freq[s[l]]
                l+=1
            freq[s[r]]=1+freq.get(s[r],0)
            res=max(res,r-l+1)
            r+=1
        return res

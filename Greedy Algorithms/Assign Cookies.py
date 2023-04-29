
class Solution:
    def maxChildren(self, N, M, greed, sz):
        
        greed.sort()
        sz.sort()
        i,j=0,0
        while i<N and j<M:
            if sz[j]>=greed[i]:
                i+=1
            j+=1
        return i

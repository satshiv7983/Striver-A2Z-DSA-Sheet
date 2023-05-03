class Solution:
    def findPath(self, m, n):
        res=[]
        
        def backtrack(r,c,cur):
            if r<0 or r>=len(m) or c<0 or c>=len(m[0]) or m[r][c]==0:
                return
            if r==c==n-1:
                res.append(cur[:])
                return 
            m[r][c]=0
            backtrack(r+1,c,cur+'D')
            backtrack(r,c-1,cur+'L')
            backtrack(r,c+1,cur+'R')
            backtrack(r-1,c,cur+'U')
            m[r][c]=1
        backtrack(0,0,'')
        return res if res else [-1]
                

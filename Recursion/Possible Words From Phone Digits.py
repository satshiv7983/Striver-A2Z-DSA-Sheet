class Solution:
    
    #Function to find list of all words possible by pressing given numbers.
    def possibleWords(self,a,N):
        d={2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
        res=[]
        def dfs(cur,idx):
            if idx>=N:
                res.append(cur[:])
                return
            s=d[a[idx]]
            for i in range(len(s)):
                cur+=s[i]
                dfs(cur,idx+1)
                cur=cur[:len(cur)-1]
        dfs("",0)
        return res

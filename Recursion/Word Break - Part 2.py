
class Solution:
    def wordBreak(self, n, dict, s):
        
        res=[]
        def backtrack(pos,sub,s):
            if pos==len(s):
                copy=(" ".join(sub))
                res.append(copy)
                return
            for idx in range(pos,len(s)):
                temp=s[pos:idx+1]
                if temp not in dict:
                    continue
                sub.append(temp)
                backtrack(idx+1,sub,s)
                sub.pop()
        backtrack(0,[],s)
        return res

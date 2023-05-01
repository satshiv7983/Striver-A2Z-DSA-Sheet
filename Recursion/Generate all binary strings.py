
class Solution:
    def generateBinaryStrings(self, n):
        
        res=[]
        def recur(string):
            if len(string)==n:
                res.append(string[:])
                return
            if not string or string[-1]=='0':
                recur(string+'1')
                recur(string+'0')
            else:
                recur(string+'0')
        recur('')
        res.sort()
        return res

#User function Template for python3

class Solution:
    def maxDepth(self, s):
        count=0
        res=0
        for i in s:
            if i=="(":
                count+=1
                res=max(res,count)
            if i==")":
                count-=1
        if count==0:
            return res
        

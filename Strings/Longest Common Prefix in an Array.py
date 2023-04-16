
class Solution:
    def longestCommonPrefix(self, arr, n):
        minl=9999999
        for i in arr:
            if len(i)<minl:
                m=i
                minl=len(i)
        a=m
        for i in range(len(a)-1,-1,-1):
            flag=True
            for j in arr:
                if j[i]!=a[i]:
                    flag=False
                    break
            if flag:
                return a[:i+1]
        return -1

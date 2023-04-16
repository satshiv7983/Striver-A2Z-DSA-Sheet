class Solution:
    def maxOdd(self, s):
        p = -1
        for i in range(len(s)-1, -1, -1):
            if int(s[i])&1:
                p = i
                break
        if p == -1:
            return ''
        return s[:p+1]

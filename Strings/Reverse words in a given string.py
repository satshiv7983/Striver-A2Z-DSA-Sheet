class Solution:
    
    #Function to reverse words in a given string.
    def reverseWords(self,s):
        a=s.split('.')
        res=".".join(reversed(a))
        return res

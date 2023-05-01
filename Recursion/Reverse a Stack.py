#User function Template for python3

from typing import List

class Solution:
    def reverse(self,st): 
        #
        def insert(stack,ele):
            if len(stack)==0:
                stack.append(ele)
                return
            x=stack.pop()
            insert(stack,ele)
            stack.append(x)
        
        def backtrack(stack):
            if len(stack)==1:
                return
            x=stack.pop()
            backtrack(stack)
            insert(stack,x)
        backtrack(st)
        return st
                

class Solution:
    # your task is to complete this function
    # function sort the stack such that top element is max
    # funciton should return nothing
    # s is a stack
    def sorted(self, s):
        
        def insert(arr,ele):
            if len(arr)==0 or arr[-1]<=ele:
                arr.append(ele)
                return
            x=arr.pop()
            insert(arr,ele)
            arr.append(x)
            
        def backtrack(stack):
            if len(stack)==1:
                return
            ele=stack.pop()
            backtrack(stack)
            insert(stack,ele)
            
        backtrack(s)

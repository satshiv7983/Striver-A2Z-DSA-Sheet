
class Solution:
    
    #Function to return a list of indexes denoting the required 
    #combinations whose sum is equal to given number.
    def combinationalSum(self,A, B):
        A=list(sorted(set(A)))
        res=[]
        def backtrack(arr,idx,cursum):
            if cursum==B:
                res.append(arr.copy())
                return
            if idx>=len(A) or cursum>B:
                return 
            arr.append(A[idx])
            backtrack(arr,idx,cursum+A[idx])
            arr.pop()
            backtrack(arr,idx+1,cursum)
        backtrack([],0,0)
        return res
            

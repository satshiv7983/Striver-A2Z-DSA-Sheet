
class Solution:
    def combinationSum(self, k, target):
        
        arr=[i for i in range(1,10)]
        res=[]
        def backtrack(subset,idx,sum,count):
            if count==k and sum==target:
                res.append(subset[:])
                return
            if idx>=len(arr) or count>k or target<0 :
                return
            subset.append(arr[idx])
            backtrack(subset,idx+1,sum+arr[idx],count+1)
            subset.pop()
            backtrack(subset,idx+1,sum,count)
        backtrack([],0,0,0)
        return res

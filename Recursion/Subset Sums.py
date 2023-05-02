class Solution:
	def subsetSums(self, arr, N):
		res=[]
		def backtrack(cursum,idx):
		    if idx>=N:
		        res.append(cursum)
		        return 
		    backtrack(cursum+arr[idx],idx+1)
		    backtrack(cursum,idx+1)
		backtrack(0,0)
		return res
		    

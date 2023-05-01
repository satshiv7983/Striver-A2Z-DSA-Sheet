class Solution:
	def AllPossibleStrings(self, s):
		n=len(s)
		res=[]
	    def recur(st,idx):
	        if idx==n:
	            res.append("".join(st))
	            return
	        st.append(s[idx])
	        recur(st,idx+1)
	        st.pop()
	        recur(st,idx+1)
        recur([],0)
        res.pop()
    	return sorted(res)

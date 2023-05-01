class Solution:
    def isValid(self,N,D):
        dig=N%10
        sum=dig
        if(dig==D):
            return False
        N//=10    
        while(N>0):
            dig=N%10
            if(dig==D or dig<=sum):
                return False
            sum+=dig
            N//=10
        return True    
    def goodNumbers(self,L,R,D):
        ans=[]
        for i in range(L,R+1):
            if ob.isValid(i,D)==True:
                ans.append(i)
        return ans

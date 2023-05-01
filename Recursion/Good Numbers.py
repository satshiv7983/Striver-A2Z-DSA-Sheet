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


    # recursive approach
    class Solution:
    def goodNumbers(self,L,R,d):
        def isValid(n, d,sum):
            if n==0:
                return True
            digit = n % 10;
            if (digit == d):
                return False;
                
            if digit<=sum :
                return False
            
            
            return isValid(n//10,d,sum+digit)
                
        
        ans=[]
        for i in range(L, R + 1):
            if i%10==0 :
                if d!=0:
                    i=i//10
                    if(isValid(i, d,0)):
                        ans+=i*10,
                else:
                    continue
            else:
                if(isValid(i, d,0)):
                        ans+=i,
                
        return ans

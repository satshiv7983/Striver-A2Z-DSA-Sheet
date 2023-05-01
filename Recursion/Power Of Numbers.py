class Solution:
    #Complete this function
    def power(self,N,R):
        if R==0:
            return 1
        temp = self.power(N, R//2)
        if R%2==0:
            return (temp* temp)%(1000000007)
        else:
            return (N*temp*temp)%(1000000007)

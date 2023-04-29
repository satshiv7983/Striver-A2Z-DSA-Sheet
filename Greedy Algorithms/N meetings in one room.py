#User function Template for python3

class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        
        start, end = (list(x) for x in zip(*sorted(zip(start,end), key=lambda pair:pair[1])))
        res=1
        j=0
        for i in range(1,n):
            if start[i]>end[j]:
                res+=1
                j=i
        return res
            

#User function Template for python3

class Solution:
    
    #Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self,jobs,n):
        
        jobs.sort(key=lambda x: x.profit, reverse=True)
        maxi = jobs[0].deadline
        for i in range(1, len(jobs)):
            maxi = max(maxi, jobs[i].deadline)
        
        slots=[-1]*(maxi+1)
        
        max_profit=0
        no=0
        for i in range(n):
            for j in range(jobs[i].deadline,0,-1):
                if slots[j]==-1:
                    slots[j]=i
                    no+=1
                    max_profit+=jobs[i].profit
                    break
        return no,max_profit
                
        

from math import floor
class Solution:
    def solve(self, bt):
        n = len(bt)
        bt.sort()
        curr_time = 0
        summ = 0
        for i in range(n):
            curr_time+=bt[i]
            #Wieght time =  turn about time - burst time
            #Since arrival time is 0, therefore turn about time is equal to completion time
            bt[i] = curr_time-bt[i]
            summ+=bt[i]
        return floor(summ/n)
        

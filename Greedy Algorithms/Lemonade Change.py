from collections import defaultdict
class Solution:
    def lemonadeChange(self, N, bills):
        change=defaultdict(int)
        for i in bills:
            if i==5:
                change[i]=1+change.get(i,0)
            elif i==10:
                if change[5]!=0:
                    change[5]-=1
                    change[10]=1+change.get(10,0)
                else:
                    return False
            elif i==20:
                if change[10]>=1 and change[5]>=1:
                    change[10]-=1
                    change[5]-=1
                elif change[5]>=3:
                    change[5]-=3
                else:
                    return False
        return True

#User function Template for python3
class stack:
    def __init__(self):
        self.s=[]
        self.minEle=None

    def push(self,x):
        self.s.append(x)
        #print(self.s)
        #CODE HERE

    def pop(self):
        if (len(self.s) != 0):
            k = self.s.pop()
        else:
            k = -1
        return k
        #CODE HERE
        

    def getMin(self):
        if (len(self.s) == 0):
            return -1
        return min(self.s)

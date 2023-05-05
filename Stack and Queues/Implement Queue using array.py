class MyQueue:
    
    def __init__(self):
        self.arr=list()
        self.head=0
        self.tail=0
        self.maxl=100003
    def push(self, x):
        
        if self.size()>=self.maxl:
            return -1
        self.arr.append(x)
        self.tail+=1

    #Function to pop an element from queue and return that element.
    def pop(self): 
        if self.size()<=0:
            self.reset()
            return -1
        data=self.arr[self.head]
        self.head+=1
        
        return data
        
    def size(self):
        return self.tail - self.head
    
    def reset(self):
        self.arr=[]
        self.head=self.tail=0

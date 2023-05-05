
class Queue:
    def __init__(self):
        self.st1=[]
        self.st2=[]
    def enqueue(self,X):
        while self.st2:
            self.st1.append(self.st2.pop())
        self.st2.append(X)
        while self.st1:
            self.st2.append(self.st1.pop())
    def dequeue(self):
        if self.st2:
            return self.st2.pop()
        else:
            return -1

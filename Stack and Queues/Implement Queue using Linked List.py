class Node: 
      
    def __init__(self, data): 
        self.data = data 
        self.next = None
        
class MyQueue: 
      
    def __init__(self): 
        self.front = self.rear = None
  
    def isEmpty(self): 
        return self.front == None
      
    #Function to push an element into the queue.
    def push(self, item): 
        temp = Node(item) 
        
        #if queue is empty, then new node is front and rear both.
        if self.rear == None: 
            self.front = self.rear = temp 
            return
        
        #adding the new node at the end of queue and changing rear.
        self.rear.next = temp 
        self.rear = temp 
  
    #Function to pop front element from the queue. 
    def pop(self): 
         
        #if queue is empty, we return -1. 
        if self.isEmpty(): 
            return -1
            
        #we delete front and update front as new temp(temp.next).
        temp = self.front 
        self.front = temp.next
  
        #if front is NULL, we also make rear as NULL.
        if(self.front == None): 
            self.rear = None
            
        #returning the popped element.
        return str(temp.data) 

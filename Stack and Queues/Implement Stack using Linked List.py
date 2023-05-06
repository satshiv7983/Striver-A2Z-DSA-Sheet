class MyStack:
    def __init__(self):
        self.root = None
    # class StackNode:

    # # Constructor to initialize a node
    # def __init__(self, data):
    #     self.data = data
    #     self.next = None
        
    #Function to push an integer into the stack.
    def __init__(self):
        self.root = None

    def isEmpty(self):
        return self.root is None

    #Function to push an integer into the stack.
    def push(self, data):
        
        #creating a new temp node in the stack
        newNode = StackNode(data)
        #assigning link part of new node to top and making it top node.
        newNode.next = self.root
        self.root = newNode
        return
    
    #Function to remove an item from top of the stack.
    def pop(self):
        
        #if node at temp pointer is null, the stack is empty so we return -1.
        if (self.isEmpty()):
            return -1
            
        #storing the data at top node and deleting that node.
        temp = self.root
        self.root = self.root.next
        popped = temp.data
        
        #returning the data.
        return popped
        

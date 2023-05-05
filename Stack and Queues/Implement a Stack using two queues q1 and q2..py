#User function Template for python3
'''
    :param x: value to be inserted
    :return: None

    queue_1 = [] # first queue
    queue_2 = [] # second queue
   '''
   
#Function to push an element into stack using two queues.
def push(x):
    
    # global declaration
    global queue_1
    global queue_2
    
    queue_2.append(x)
    while queue_1:
        queue_2.append(queue_1.pop(0))
    queue_2,queue_1=queue_1,queue_2
 # code here


#Function to pop an element from stack using two queues.     
def pop():
    
    # global declaration
    global queue_1
    global queue_2
    
    if queue_1:
        return queue_1.pop(0)
    else:
        return -1

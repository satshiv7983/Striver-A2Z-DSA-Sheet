#Function to find the data of nth node from the end of a linked list
def getNthFromLast(head,n):
    temp=head
    c=1
    while True:
        if c==n:
            break
        if not temp:
            return -1
        temp=temp.next
        c+=1
    if not temp:
        return -1
    begin=head
    while temp and temp.next:
        if not temp:
            return -1
        begin=begin.next
        temp=temp.next
    return begin.data

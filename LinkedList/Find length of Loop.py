
def countNodesinLoop(head):
    if head is None:
        return 0
    slow=head
    fast=head
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
        if slow==fast:
            break
    if not fast or not fast.next:
        return 0
    temp=head
    while temp!=slow:
        temp=temp.next
        slow=slow.next
    start=temp
    count=0
    while True:
        temp=temp.next
        count+=1
        if temp==start:
            break
    return count

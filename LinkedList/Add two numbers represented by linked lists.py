class Solution:
    #Function to add two numbers represented by linked list.
    def addTwoLists(self, first, second):
        def reverse(head):
            prev=None
            while head:
                temp=head.next
                head.next=prev
                prev=head
                head=temp
            return prev
        
        node1=reverse(first)
        node2=reverse(second)
        carry=0
        dummy=Node(0)
        newnode=dummy
        while node1 and node2:
            x=node1.data+node2.data+carry
            dat=x%10
            carry=x//10
            temp=Node(dat)
            newnode.next=temp
            newnode=temp
            node1=node1.next
            node2=node2.next
        while node1:
            x=node1.data+carry
            node1.data=(x)%10
            carry=x//10
            newnode.next=node1
            newnode=node1
            node1=node1.next
        while node2:
            x=node2.data+carry
            node2.data=(x)%10
            carry=x//10
            newnode.next=node2
            newnode=node2
            node2=node2.next
        if carry:
            newnode.next=Node(1)
        res=reverse(dummy.next)
        return res
            

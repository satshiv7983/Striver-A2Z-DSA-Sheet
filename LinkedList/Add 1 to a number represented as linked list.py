class Solution:
    def addOne(self,head):
        def reverse(head):
            prev=None
            while head:
                temp=head.next
                head.next=prev
                prev=head
                head=temp
            return prev
        node=reverse(head)
        carry=1
        temp=node
        while temp:
            prev=temp
            x=(temp.data+carry)
            temp.data=x%10
            carry=x//10
            temp=temp.next
            
        if carry==1:
            prev.next=Node(1)
        res=reverse(node)
        return res

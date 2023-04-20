class Solution:
    
    #Function to rotate a linked list.
    def rotate(self, head, k):
        def reverse(head):
            prev=None
            while head:
                temp=head.next
                head.next=prev
                prev=head
                head=temp
            return prev
        temp=head
        c=1
        while True:
            if c==k:
                break
            temp=temp.next
            c+=1
        bed=temp.next
        temp.next=None
        node2=reverse(bed)
        node1=reverse(head)
        
        pet=node1
        while pet:
            pre=pet
            pet=pet.next
        pre.next=node2
        
        result=reverse(node1)
        return result

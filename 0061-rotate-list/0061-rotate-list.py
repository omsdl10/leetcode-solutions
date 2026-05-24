# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def rotate(head):
    newnode=head
    while newnode.next:
        newnode=newnode.next
    new=head
    while new!=newnode:
        new=new.next
    new.next=None
    newnode.next=head
    head=newnode
    return head

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k==0 or head is None or head.next is None:
            return head
        tail=head 
        count=1
        while tail.next:
            tail=tail.next
            count+=1
        tail.next=head
        hlen=count-(k%count)
        while hlen-1:
            head=head.next
            hlen-=1
        newnode=head.next
        head.next=None
        head=newnode
        return head

    



    
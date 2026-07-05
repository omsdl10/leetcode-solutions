# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def reverse(head):
    if not head:
        return head
    prev=None
    node=head
    while node:
        nextnode=node.next
        node.next=prev
        prev=node
        node=nextnode
    return prev
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        if not head or head.next==None:
            return head.val
        count=0
        i=0
        node=reverse(head)
        while node:
            count=count+node.val*(2**i)
            i+=1
            node=node.next 
        return count 
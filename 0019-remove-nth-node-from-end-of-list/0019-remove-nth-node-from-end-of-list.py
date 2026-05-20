# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node=head
        count=0
        while node:
            count+=1
            node=node.next
        if (count==1 and n==1) or count==n:
            return head.next
        curr=head
        newcount=0
        while curr:
            newcount+=1
            if newcount==count-n:
                curr.next=curr.next.next
            curr=curr.next
        return head



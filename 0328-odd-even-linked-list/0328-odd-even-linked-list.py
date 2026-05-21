# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        odd=head
        even=head.next
        curr1=odd
        curr2=even
        while curr2 and curr2.next:
            curr1.next=curr2.next
            curr1=curr1.next
            curr2.next=curr1.next
            curr2=curr2.next
        curr1.next=even
        return odd


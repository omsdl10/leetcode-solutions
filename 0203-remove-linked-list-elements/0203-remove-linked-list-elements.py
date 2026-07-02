# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head and head.val==val :
            head=head.next
        if head is None or head.next is None:
            if head and head.val==val:return head.next
            return head
        node=head
        while node.next is not None:
            if node.next.val==val:
                node.next=node.next.next
                continue
            node=node.next
        return head

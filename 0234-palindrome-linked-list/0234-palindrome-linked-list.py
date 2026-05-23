# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        curr=slow
        prev=None
        while curr is not None:
            newnode=curr.next
            curr.next=prev
            prev=curr
            curr=newnode
        n1=head
        n2=prev
        while n1 and n2:
            if n1.val!=n2.val:
                return False
            n1=n1.next
            n2=n2.next
        return True
        
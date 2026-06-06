# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def split(head):
    slow=head 
    fast=head.next
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
    second=slow.next
    slow.next=None
    return second
    

def merge(first, second):
    if not first:
        return second
    if not second:
        return first
    if first.val<second.val:
        first.next=merge(first.next,second)
        return first
    else:
        second.next=merge(first,second.next)
        return second
  

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        second = split(head)
        head = self.sortList(head)
        second = self.sortList(second)
        return merge(head, second)
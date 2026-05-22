# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head
        slow=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        
        mid_head = slow.next
        slow.next=None

        prev=None
        cur=mid_head

        while cur:
            nxt=cur.next
            cur.next=prev
            prev=cur
            cur=nxt
        
        mid_head=prev
        first=head
        while mid_head:
            first_nxt= first.next
            second_nxt=mid_head.next

            first.next=mid_head
            mid_head.next=first_nxt

            first=first_nxt
            mid_head=second_nxt


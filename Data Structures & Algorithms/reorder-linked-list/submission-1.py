# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast=head
        slow=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        
        dummy2=slow.next
        slow.next=None

        pre=None
        cur=dummy2
        while cur:
            nxt=cur.next
            cur.next=pre
            pre=cur
            cur=nxt
        
        dummy2=pre
        dummy1=head
        while dummy2:
            dummy1_nxt=dummy1.next
            dummy2_nxt=dummy2.next

            dummy1.next=dummy2
            dummy2.next=dummy1_nxt

            dummy1=dummy1_nxt
            dummy2=dummy2_nxt
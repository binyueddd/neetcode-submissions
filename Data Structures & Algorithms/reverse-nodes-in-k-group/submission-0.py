# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        
        # def reverselist(head):
        #     pre=None
        #     cur=head
        #     while cur:
        #         nxt=cur.next
        #         cur.next=pre
        #         pre=cur
        #         cur=nxt
        #     return pre
        
        dummy=ListNode(0,head)
        prev_head=dummy
        k_node=prev_head
        while True:
            count=k
            while k_node and count>0:
                k_node=k_node.next
                count-=1
            
            if not k_node:
                break
            
            group_next=k_node.next
            old_group_head = prev_head.next
            prev = group_next
            cur = prev_head.next

            while cur!=group_next:
                nxt=cur.next
                cur.next=prev
                prev=cur
                cur=nxt
            
            prev_head.next = k_node
            prev_head = old_group_head
            k_node = prev_head
        return dummy.next
            

            

            

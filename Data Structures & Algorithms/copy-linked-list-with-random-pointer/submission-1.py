"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        cur=head
        while cur:
            new=Node(cur.val)
            new.next=cur.next
            cur.next=new
            cur=new.next
        
        cur=head
        while cur:
            new=cur.next
            if cur.random:
                new.random=cur.random.next
            cur=new.next

        cur=head
        new_head=cur.next

        while cur:
            new=cur.next
            cur.next=new.next
            if new.next:
                new.next=new.next.next
            cur=cur.next
        return new_head
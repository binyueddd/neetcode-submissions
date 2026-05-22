# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap=[]
        counter=0
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, counter, node)) #记得i，不然无法处理两个val相同情况
                counter+=1
        dummy=ListNode(0)
        cur=dummy

        while heap:
            val,_,node=heapq.heappop(heap)
            cur.next=node
            cur=cur.next
            if node.next:
                heapq.heappush(heap,(node.next.val, counter, node.next))
                counter+=1
            
        return dummy.next
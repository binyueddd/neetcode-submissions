# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        def merge2lists(list1, list2):
            dummy=ListNode(0)
            cur=dummy
            while list1 and list2:
                if list1.val<=list2.val:
                    cur.next=list1
                    list1=list1.next
                    cur=cur.next
                else:
                    cur.next=list2
                    list2=list2.next
                    cur=cur.next
            
            if list1:
                cur.next=list1
            if list2:
                cur.next=list2
    
            return dummy.next
        
        k=len(lists)
        interval=1

        while interval<k:
            for i in range(0, k-interval, interval*2):
                lists[i]=merge2lists(lists[i],lists[i+interval])
        
            interval*=2
        return lists[0]


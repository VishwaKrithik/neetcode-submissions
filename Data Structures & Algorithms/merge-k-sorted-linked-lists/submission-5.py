# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        heap = []

        for ll in lists:
            while ll:
                heap.append(ll.val)
                ll = ll.next

        heapq.heapify(heap)

        dummy = ListNode(0)
        curr = dummy

        while heap:
            curr.next = ListNode(heapq.heappop(heap))
            curr = curr.next
        
        return dummy.next
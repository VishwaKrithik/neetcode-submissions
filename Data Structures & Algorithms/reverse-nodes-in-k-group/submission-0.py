# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head or k == 1:
            return head
        
        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next
            
            group_next = kth.next

            prev, curr = group_next, group_prev.next
            while curr != group_next:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            
            tail = group_prev.next
            group_prev.next = kth
            group_prev = tail
    
        
        # dummy = temp = ListNode(0, head)
        # start = temp
        # temp = temp.next

        # while temp:
        #     n = 0
        #     prev = None
        #     curr = end = temp

        #     while curr and n < k:
        #         nxt = curr.next
        #         curr.next = prev
        #         prev = curr
        #         curr = nxt
        #         n += 1
            
        #     temp = curr
        #     start.next = prev
        #     end.next = curr
        #     start = end
        
        # return dummy.next
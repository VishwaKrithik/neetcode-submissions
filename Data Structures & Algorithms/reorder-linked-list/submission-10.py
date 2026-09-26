# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        curr = slow.next
        slow.next = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        slow1 = head
        slow2 = prev
        while slow2:
            temp1 = slow1.next
            temp2 = slow2.next

            slow1.next = slow2
            slow2.next = temp1
            
            slow1 = temp1
            slow2 = temp2
        
        
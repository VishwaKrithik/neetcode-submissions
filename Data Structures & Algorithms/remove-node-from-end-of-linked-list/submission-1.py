# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        length = 0
        temp = head

        while temp:
            length += 1
            temp = temp.next
        
        req = length - n
        if req == 0:
            return head.next

        temp = head
        cur = head
        for i in range(length - 1):
            if i + 1 == req:
                cur.next = cur.next.next
                break
            cur = cur.next
        return head
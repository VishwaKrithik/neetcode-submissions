# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # Recursion
        def recursion(node):
            if not node:
                return None
            
            head = node
            if node.next:
                head = recursion(node.next)
                node.next.next = node
                node.next = None
            
            return head


        return recursion(head)


        # Iterative
        """prev = None
        cur = head
        nxt = None
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        
        return prev"""
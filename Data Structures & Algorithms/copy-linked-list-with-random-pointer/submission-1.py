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
        
        dummy = Node(0, None)
        curr = dummy
        temp = head
        rando = {}

        while temp:
            curr.next = Node(temp.val, None, temp.random)
            curr = curr.next
            rando[temp] = curr
            temp = temp.next

        curr = dummy.next
        while curr:
            if curr.random is not None:
                curr.random  = rando[curr.random]
            curr = curr.next
        
        return dummy.next

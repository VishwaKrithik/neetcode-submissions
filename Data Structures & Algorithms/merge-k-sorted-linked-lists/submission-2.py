# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        head = ListNode(0)
        dummy = head

        arr = []
        for i in lists:
            while i:
                arr.append(i.val)
                i = i.next
        
        arr.sort()

        for num in arr:
            head.next = ListNode(num)
            head = head.next
        
        return dummy.next

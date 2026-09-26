# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        array = []

        temp = head

        while temp:
            array.append(temp.val)
            temp = temp.next
        array.sort()    
        temp = head
        idx = 0
        while temp:
            temp.val = array[idx]
            idx += 1
            temp = temp.next
        
        return head
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return
        
        arr = []
        temp = head

        while temp:
            arr.append(temp)
            temp = temp.next

        for i in range(len(arr) - 1, 0, -1):
            arr[i].next = arr[i - 1]
            arr[i - 1].next = None
        
        return arr[-1]
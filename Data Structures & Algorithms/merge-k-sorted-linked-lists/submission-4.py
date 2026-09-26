# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        arr = []

        for ll in lists:
            while ll:
                arr.append(ll)
                ll = ll.next
        
        arr.sort(key = lambda x: x.val)

        for i in range(len(arr) - 1):
            arr[i].next = arr[i + 1]
        
        return arr[0] if arr else None

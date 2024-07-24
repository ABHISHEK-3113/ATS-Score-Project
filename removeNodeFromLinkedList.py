# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        if not head:
            return None
        
       
        curr = head 
        temp = ListNode(-1, head) 
        prev = temp

        while curr:

            if curr.val != val:
                prev = curr 
            else:
                prev.next = curr.next 
            curr = curr.next 
        
        return temp.next

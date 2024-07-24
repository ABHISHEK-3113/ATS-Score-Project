# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        carry = 0
        ans = ListNode()
        d1 = l1 
        d2 = l2 
        prev = ans 
        sm = 0
        while d1 or d2 or carry != 0: 
            digit1 = d1.val if d1 else 0 
            digit2 = d2.val if d2 else 0 
            
            sm = digit1 + digit2 + carry 

            digit = sm % 10 
            carry = sm // 10
            
            newNode = ListNode(digit)

            prev.next = newNode 
            prev = prev.next 
                        
            if d1:
                d1 = d1.next 
            
            if d2:
                d2 = d2.next   
            
        prev.next = None
        return ans.next

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num = (l1.val + l2.val) % 10
        carry = (l1.val + l2.val) // 10
        head = ListNode(num)

        current = head
        current1 = l1.next
        current2 = l2.next     
        
        while current1 or current2 or carry:
            val1 = 0
            val2 = 0
            
            if current1:
                val1 = current1.val
                
            if current2:
                val2 = current2.val
                
            num = (val1 + val2 + carry) % 10
            carry = (val1 + val2 + carry) // 10
            current.next = ListNode(num)
            
            current = current.next
            if current1:
                current1 = current1.next
                
            if current2:
                current2 = current2.next
        return head
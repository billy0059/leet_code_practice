# https://leetcode.com/problems/add-two-numbers/description/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        node = ListNode()
        ret_head_node = node
        
        while l1 or l2 or carry:
            if l1 and l2:
                sum = l1.val + l2.val + carry
                carry = sum // 10
                node.val = sum % 10
                l1 = l1.next
                l2 = l2.next
            elif l1:
                sum = l1.val + carry
                carry = sum // 10
                node.val = sum % 10
                l1 = l1.next
            elif l2:
                sum = l2.val + carry
                carry = sum // 10
                node.val = sum % 10
                l2 = l2.next
            elif carry:
                node.val = carry
                carry = 0

            if l1 or l2 or carry:
                node.next = ListNode()
                node = node.next
        return ret_head_node
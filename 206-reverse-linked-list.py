# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head: # Reverse the linked list, we need two variables to do: prev and next
            next_node = head.next # First store the next node from head.next
            head.next = prev # Then set head.next to previous node
            prev = head # Now update the previous node to current for following process
            head = next_node # Now set head to next node and continue the reverse process
        head = prev # The head after the reverse process would be NULL, now update it with the previous node,
                    # which is the new head

        return head
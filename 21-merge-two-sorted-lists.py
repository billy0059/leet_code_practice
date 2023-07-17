# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        elif list2 == None:
            return list1

        # Set the return head, determined by the smaller head.val
        if list1.val <= list2.val:
            ret_head = list1
            list1 = list1.next
        else:
            ret_head = list2
            list2 = list2.next
        tail = ret_head

        while list1 and list2:
            if list1.val <= list2.val: # Insert list1 to the return linked list
                tail.next = list1
                tail = list1
                list1 = list1.next
            else: # Insert list2 to the return linked list
                tail.next = list2
                tail = list2
                list2 = list2.next
        if list1 != None:
            tail.next = list1
        elif list2 != None:
            tail.next = list2
        return ret_head
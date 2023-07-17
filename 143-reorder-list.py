# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        node_list = []
        node = head
        while node != None:
            node_list.append(node)
            node = node.next
        l, r = 0, len(node_list)-1
        for i in range(math.ceil(len(node_list)/2)-1): # The insert time is "math.ceil(len(node_list)/2)-1"
            # Insert node_list[r] in to node_list[l] and node_list[l+1]
            node_list[l].next = node_list[r]
            node_list[r].next = node_list[l+1]
            node_list[r-1].next = None # update new tail
            # Update new position
            l = l + 1
            r = r - 1

# https://leetcode.com/problems/binary-tree-preorder-traversal/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return_list = []
        traversed_stack = []
        if root:
            traversed_stack.append(root)
        else:
            return []
        while traversed_stack:
            node = traversed_stack.pop()
            return_list.append(node.val)
            if node.right:
                traversed_stack.append(node.right)
            if node.left:
                traversed_stack.append(node.left)
        return return_list
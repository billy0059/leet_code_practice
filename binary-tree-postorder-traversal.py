# https://leetcode.com/problems/binary-tree-postorder-traversal/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return_list = []
        travered_nodes = []
        visited_node = None
        while root or travered_nodes:
            if root:
                travered_nodes.append(root)
                root = root.left
            else:
                node = travered_nodes[-1]
                if node.right and node.right != visited_node:
                    root = node.right
                else:
                    return_list.append(node.val)
                    visited_node = travered_nodes.pop()
        return return_list
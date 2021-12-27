#https://leetcode.com/problems/binary-tree-inorder-traversal/
#Given the root of a binary tree, return the inorder traversal of its nodes' values.
from typing import Optional
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        inoder_traverse_stack=[]
        res_list=[]
        while root or len(inoder_traverse_stack)!=0:
            if root:
                inoder_traverse_stack.append(root)
                root = root.left
            else:
                node=inoder_traverse_stack.pop()
                res_list.append(node.val)
                root=node.right
        return res_list

        '''
        # Recursive method:
        def inorder_recursive(res_list, node):
            if node:
                inorder_recursive(res_list, node.left)
                res_list.append(node.val)
                inorder_recursive(res_list, node.right)
        res_list=[]
        inorder_recursive(res_list, root)
        return res_list
        '''

def main():
    root = TreeNode(1, left=None, right=TreeNode(2, left=TreeNode(3)))
    solution = Solution()
    print(solution.inorderTraversal(root))


if __name__ == '__main__':
    main()
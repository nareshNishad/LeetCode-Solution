#
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        out, stack = [], [root]
        while stack:
            node = stack.pop()
            if node:
                out.append(node.val)
                stack.append(node.left)
                stack.append(node.right)

        return out[::-1]
# @lc code=end


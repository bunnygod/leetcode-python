# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        def pushleft(node: TreeNode, stack: List[TreeNode]):
            while node:
                stack.append(node)
                node = node.left

        stack, range_sum = [], 0
        pushleft(root, stack)

        while stack:
            node = stack.pop()

            if low <= node.val <= high:
                range_sum += node.val
            elif node.val > high:
                break

            pushleft(node.right, stack)

        return range_sum

class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        def in_order(node):
            nonlocal range_sum

            if node:
                in_order(node.left)

                if low <= node.val <= high:
                    range_sum += node.val

                in_order(node.right)

        range_sum = 0
        in_order(root)
        return range_sum

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def pathSum(self, root, targetSum):

        if not root:
            return None

        result = []
        num_list = []

        def dfs(root, targetSum):
            
            num_list.append(root.val)

            if root.left is None and root.right is None:
                if sum(num_list) == targetSum:
                    result.append(num_list[:])

            else:
                if root.left is not None:
                    dfs(root.left, targetSum)
                if root.right is not None:
                    dfs(root.right, targetSum)
                
            num_list.pop()
            
        dfs(root, targetSum)

        return result

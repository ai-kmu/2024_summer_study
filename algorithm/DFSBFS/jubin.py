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

        def dfs(root, targetSum, current_sum):
            
            num_list.append(root.val)
            current_sum += root.val

            if root.left is None and root.right is None:
                if current_sum == targetSum:
                    result.append(num_list[:])

            else:
                if root.left is not None:
                    dfs(root.left, targetSum, current_sum)
                if root.right is not None:
                    dfs(root.right, targetSum, current_sum)
                
            num_list.pop()
            current_sum -= root.val
            
        dfs(root, targetSum, 0)

        return result

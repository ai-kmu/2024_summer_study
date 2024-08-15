# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        def dfs(node, visited, cursum):
            
            if node is None:
                return

            visited.append(node.val)
            cursum += node.val

            if node.left is None and node.right is None and cursum == targetSum:
                result.append(list(visited))
            else:
                dfs(node.left, visited, cursum)
                dfs(node.right, visited, cursum)
    
            visited.pop()

        result = []
        dfs(root, [], 0)

        return result

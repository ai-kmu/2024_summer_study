# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(node, curr_sum, path):
            if not node:
                return
            curr_sum += node.val
            path.append(node.val)

            if (not node.left) and (not node.right) and (curr_sum == targetSum):
                res.append(path[:])
            dfs(node.left, curr_sum, path)
            dfs(node.right, curr_sum, path)
            path.pop()
        res = []
        dfs(root, 0, [])
        return res

# node: 5, curr_sum: 0, path: []
# search left sub tree
# node: 4, curr_sum: 5, path: [5]
# node: 11, curr_sum: 9, path: [5,4]
# search left sub tree
# node: 7, curr_sum: 20, path: [5,4,11]
# curr_sum = 27 not eq targetSum then pop 7
# node: 2, curr_sum: 20, path: [5,4,11]
# curr_sum = 22 and eq targetSum and not 2.left and not 2.right -> is leaf node
# res: [5,4,11,2]

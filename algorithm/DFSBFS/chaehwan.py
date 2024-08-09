import copy
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        
        if not root:
            return([])

        answer = []
        def dfs(root, targetSum, nodeList):

            tmp = copy.deepcopy(nodeList)
            tmp.append(root.val)

            if root.left is None and root.right is None:
                print( root.val, tmp, nodeList)
                if targetSum == sum(tmp):
                    answer.append(tmp)

            if root.left is not None:
                dfs(root.left, targetSum, tmp)
            if root.right is not None:
                dfs(root.right, targetSum, tmp)
                
        dfs(root, targetSum, [])

        return answer
                    

            
        

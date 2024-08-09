# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #root = tree임. 
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        ans = []
        #빈 tree가 들어올 때.
        if(root == None):
            return ans

        def dfs(node, current_node, sum):

            #leaf node 이어야 함.
            if(node.left == None and node.right == None):

                current_node += [node.val]
                sum += node.val

                if(sum == targetSum):
                    ans.append(current_node)
                    return
            
            
            if(node.left != None):
                dfs(node.left, current_node + [node.val], sum + node.val)
            
            if(node.right != None):
                dfs(node.right, current_node + [node.val], sum + node.val)

        dfs(root, [], 0)
        
        return ans

            

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        res = []
        if root == None :
             return None
            
        if root.left == None and root.right == None : 
            if root.val == targetSum : 
                res.append([root.val])     
            return res
          
        def DFS(root : TreeNode, val, targetSum,dis,res) :
            if root :
                dis.append(root.val)
                root.val = root.val + val
                
                if root.val == targetSum and root.left == None and root.right ==None: 
                    res.append(dis)
                else : 
                    DFS(root.left,root.val,targetSum,dis[:],res)
                    DFS(root.right,root.val,targetSum,dis[:],res)
        
        
        DFS(root.left,root.val,targetSum,[root.val],res)
        DFS(root.right,root.val,targetSum,[root.val],res)
        
        return res 

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        def dfs(root, path):

            if not root:
                return

            path.append(root.val)

            if not root.left and not root.right:
                if sum(path)==targetSum:
                    result.append(list(path))

            dfs(root.left, path)
            dfs(root.right, path)
            path.pop()
            return
        
        result = []
        dfs(root, [])
        return result 

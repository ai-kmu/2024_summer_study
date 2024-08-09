# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = [] # 결과 담을 리스트
        if (root == None): # 빈 입력에 대한 예외처리
            return res
        def addpath(tmp_node, path):
            path.append(tmp_node.val)
            #print(path)
            sum = 0
            if (tmp_node.left == None) & (tmp_node.right == None) : # leaf노드일 경우 sum확인
                for i in path:
                    sum+= i
                if sum == targetSum :
                    res.append(path[:])
        tmp = []
        def Search(tmp_node, tmp):
            addpath(tmp_node, tmp)
            if tmp_node.left != None :
                Search(tmp_node.left, tmp)
            if tmp_node.right != None :
                Search(tmp_node.right, tmp)
            tmp.pop()
        Search(root, tmp)

        return res

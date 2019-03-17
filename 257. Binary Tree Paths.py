# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:

        def ppath(root, path=''): #将前面的路径进行携带
            if root:
                path += str(root.val)
                if not root.left and not root.right:
                    paths.append(path)
                else:
                    path += '->'
                    ppath(root.left, path)
                    ppath(root.right, path)

        paths = []
        ppath(root)
        return paths

